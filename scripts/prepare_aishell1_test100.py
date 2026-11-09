#!/usr/bin/env python3
"""Freeze a deterministic 100-utterance AISHELL-1 official-test subset."""

from __future__ import annotations

import argparse
import csv
import random
import wave
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Record:
    utterance_id: str
    wav_path: Path
    reference_text: str


def read_transcripts(path: Path) -> dict[str, str]:
    transcripts: dict[str, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split(maxsplit=1)
        if len(fields) != 2:
            raise ValueError(f"{path}:{line_number}: expected utterance ID and transcript")
        utterance_id, reference_text = fields
        if utterance_id in transcripts:
            raise ValueError(f"{path}:{line_number}: duplicate utterance ID {utterance_id}")
        transcripts[utterance_id] = reference_text
    return transcripts


def select_records(aishell_root: Path, count: int, seed: int) -> list[Record]:
    aishell_root = aishell_root.resolve()
    transcripts = read_transcripts(aishell_root / "transcript" / "aishell_transcript_v0.8.txt")
    by_id = {path.stem: path for path in sorted((aishell_root / "wav" / "test").rglob("*.wav"))}
    if len(by_id) < count:
        raise ValueError(f"expected at least {count} official test utterances, found {len(by_id)}")
    missing = sorted(set(by_id) - set(transcripts))
    if missing:
        raise ValueError(f"missing reference text for {missing[0]}")
    selected_ids = sorted(random.Random(seed).sample(sorted(by_id), count))
    return [Record(utterance_id, by_id[utterance_id], transcripts[utterance_id]) for utterance_id in selected_ids]


def duration_seconds(wav_path: Path) -> float:
    with wave.open(str(wav_path), "rb") as handle:
        return handle.getnframes() / handle.getframerate()


def write_subset(records: list[Record], output: Path, project_root: Path) -> None:
    project_root = project_root.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["utterance_id", "audio_path", "reference_text", "duration_seconds", "source_split"], delimiter=chr(9))
        writer.writeheader()
        for record in records:
            try:
                relative_audio = record.wav_path.resolve().relative_to(project_root)
            except ValueError as error:
                raise ValueError(f"audio is outside project root: {record.wav_path}") from error
            writer.writerow({"utterance_id": record.utterance_id, "audio_path": relative_audio.as_posix(), "reference_text": record.reference_text, "duration_seconds": f"{duration_seconds(record.wav_path):.6f}", "source_split": "aishell1-test"})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aishell-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20261109)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.count <= 0:
        raise ValueError("--count must be positive")
    write_subset(select_records(args.aishell_root, args.count, args.seed), args.output, args.project_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
