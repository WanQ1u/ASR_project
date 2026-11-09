#!/usr/bin/env python3
"""Run the fixed AISHELL-1 subset with the official WeNet recognizer."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Record:
    utterance_id: str
    audio_path: Path
    reference_text: str
    duration_seconds: float


def load_subset(path: Path, project_root: Path) -> list[Record]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter=chr(9)))
    required = {"utterance_id", "audio_path", "reference_text", "duration_seconds", "source_split"}
    if not rows or set(rows[0]) != required:
        raise ValueError(f"subset header must be exactly {sorted(required)}")
    records = []
    for row in rows:
        audio_path = (project_root / row["audio_path"]).resolve()
        if not audio_path.is_file():
            raise FileNotFoundError(f"audio file does not exist: {audio_path}")
        records.append(Record(row["utterance_id"], audio_path, row["reference_text"], float(row["duration_seconds"])))
    if len({record.utterance_id for record in records}) != len(records):
        raise ValueError("subset contains duplicate utterance IDs")
    return records


def build_recognize_command(python: Path, wenet_root: Path, config: Path, checkpoint: Path, data_list: Path, result_dir: Path, gpu: int) -> list[str]:
    model_dir = config.parent
    return [
        str(python), str(wenet_root / "wenet" / "bin" / "recognize.py"),
        "--gpu", str(gpu), "--modes", "ctc_greedy_search", "--config", str(config),
        "--data_type", "raw", "--test_data", str(data_list), "--checkpoint", str(checkpoint),
        "--beam_size", "10", "--batch_size", "1", "--result_dir", str(result_dir),
        "--override_config", f"tokenizer_conf.symbol_table_path {model_dir / 'units.txt'}",
        "--override_config", f"cmvn_conf.cmvn_file {model_dir / 'global_cmvn'}",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wenet-root", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--subset", type=Path, required=True)
    parser.add_argument("--result-dir", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--gpu", type=int, default=0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.resolve()
    wenet_root = args.wenet_root.resolve()
    config = args.config.resolve()
    checkpoint = args.checkpoint.resolve()
    for artifact in (config, checkpoint, config.parent / "units.txt", config.parent / "global_cmvn"):
        if not artifact.is_file():
            raise FileNotFoundError(f"required model artifact does not exist: {artifact}")
    records = load_subset(args.subset, project_root)
    if len(records) != 100:
        raise ValueError(f"expected exactly 100 subset rows, got {len(records)}")
    args.result_dir.mkdir(parents=True, exist_ok=True)
    data_list = args.result_dir / "data.list"
    references = args.result_dir / "reference.txt"
    with data_list.open("w", encoding="utf-8") as data_handle, references.open("w", encoding="utf-8") as reference_handle:
        for record in records:
            data_handle.write(json.dumps({"key": record.utterance_id, "wav": str(record.audio_path), "txt": record.reference_text}, ensure_ascii=False) + "\n")
            reference_handle.write(f"{record.utterance_id} {record.reference_text}\n")
    command = build_recognize_command(Path(sys.executable), wenet_root, config, checkpoint, data_list.resolve(), args.result_dir.resolve(), args.gpu)
    started = time.perf_counter()
    completed = subprocess.run(command, cwd=wenet_root, check=False)
    elapsed_seconds = time.perf_counter() - started
    if completed.returncode != 0:
        return completed.returncode
    predictions = args.result_dir / "ctc_greedy_search" / "text"
    prediction_map = {}
    for line in predictions.read_text(encoding="utf-8").splitlines():
        fields = line.split(maxsplit=1)
        if len(fields) != 2 or not fields[1].strip():
            raise ValueError(f"invalid prediction row: {line!r}")
        prediction_map[fields[0]] = fields[1]
    expected_ids = {record.utterance_id for record in records}
    if set(prediction_map) != expected_ids:
        raise ValueError(f"expected {len(expected_ids)} predictions, got {len(prediction_map)}")
    with (args.result_dir / "ctc_greedy_search" / "cer.txt").open("w", encoding="utf-8") as handle:
        subprocess.run([str(Path(sys.executable)), str(wenet_root / "tools" / "compute-wer.py"), "--char=1", "--v=0", str(references), str(predictions)], check=True, stdout=handle)
    audio_seconds = sum(record.duration_seconds for record in records)
    metrics = {"input_count": len(records), "audio_seconds": audio_seconds, "wall_clock_seconds": elapsed_seconds, "rtf": elapsed_seconds / audio_seconds}
    (args.result_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
