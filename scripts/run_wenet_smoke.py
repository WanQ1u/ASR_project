#!/usr/bin/env python3
"""Run the official WeNet recognizer on a manifest of smoke-test WAV files."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wenet-root", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--result-dir", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--gpu", type=int, default=0)
    return parser.parse_args()


def load_inputs(path: Path, project_root: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    required = {"audio_path", "duration_seconds", "source_category"}
    if not rows and not path.read_text(encoding="utf-8").strip():
        raise ValueError("inputs manifest is empty")
    if set(rows[0]) != required:
        raise ValueError(f"inputs header must be exactly {sorted(required)}")
    if len(rows) != 5:
        raise ValueError(f"expected exactly five smoke-test rows, got {len(rows)}")

    records = []
    for index, row in enumerate(rows, start=1):
        relative_audio = Path(row["audio_path"])
        audio = (project_root / relative_audio).resolve()
        if not audio.is_file():
            raise FileNotFoundError(f"row {index}: audio file does not exist: {audio}")
        records.append({"key": f"smoke_{index:02d}", "wav": str(audio), "txt": ""})
    return records


def main() -> int:
    args = parse_args()
    args.wenet_root = args.wenet_root.resolve()
    args.config = args.config.resolve()
    model_dir = args.config.parent
    symbol_table = model_dir / "units.txt"
    cmvn_file = model_dir / "global_cmvn"
    for artifact in (symbol_table, cmvn_file):
        if not artifact.is_file():
            raise FileNotFoundError(f"required checkpoint artifact does not exist: {artifact}")
    records = load_inputs(args.inputs, args.project_root.resolve())
    args.result_dir.mkdir(parents=True, exist_ok=True)
    data_list = args.result_dir / "data.list"
    with data_list.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    command = [
        sys.executable,
        str(args.wenet_root / "wenet" / "bin" / "recognize.py"),
        "--gpu",
        str(args.gpu),
        "--modes",
        "ctc_greedy_search",
        "--config",
        str(args.config),
        "--data_type",
        "raw",
        "--test_data",
        str(data_list.resolve()),
        "--checkpoint",
        str(args.checkpoint.resolve()),
        "--beam_size",
        "10",
        "--batch_size",
        "1",
        "--result_dir",
        str(args.result_dir.resolve()),
        "--override_config",
        f"tokenizer_conf.symbol_table_path {symbol_table}",
        "--override_config",
        f"cmvn_conf.cmvn_file {cmvn_file}",
    ]
    print("Running official WeNet recognizer:")
    print(" ".join(command))
    completed = subprocess.run(command, cwd=args.wenet_root, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
