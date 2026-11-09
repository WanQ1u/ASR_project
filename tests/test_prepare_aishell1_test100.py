import csv
import random
import tempfile
import unittest
import wave
from pathlib import Path

from scripts.prepare_aishell1_test100 import select_records, write_subset


def write_wav(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as handle:
        handle.setnchannels(1)
        handle.setsampwidth(2)
        handle.setframerate(16000)
        handle.writeframes(b"\x00\x00" * 16000)


class PrepareAishell1Test100Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temp_dir.name)
        self.aishell_root = self.project_root / "data" / "data_aishell"
        transcript = self.aishell_root / "transcript" / "aishell_transcript_v0.8.txt"
        transcript.parent.mkdir(parents=True)
        transcript.write_text(
            "BAC009S0001W0003 第三条\n"
            "BAC009S0001W0001 第一条\n"
            "BAC009S0001W0002 第二条\n",
            encoding="utf-8",
        )
        for utterance_id in ("BAC009S0001W0003", "BAC009S0001W0001", "BAC009S0001W0002"):
            write_wav(self.aishell_root / "wav" / "test" / "S0001" / f"{utterance_id}.wav")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_select_records_uses_sorted_candidates_and_fixed_seed(self) -> None:
        selected = select_records(self.aishell_root, count=2, seed=17)

        candidates = ["BAC009S0001W0001", "BAC009S0001W0002", "BAC009S0001W0003"]
        expected_ids = sorted(random.Random(17).sample(candidates, 2))
        self.assertEqual([record.utterance_id for record in selected], expected_ids)

    def test_write_subset_records_relative_paths_and_durations(self) -> None:
        output = self.project_root / "subset.tsv"

        write_subset(
            select_records(self.aishell_root, count=2, seed=17),
            output=output,
            project_root=self.project_root,
        )

        with output.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["audio_path"].split("/")[0], "data")
        self.assertEqual(rows[0]["duration_seconds"], "1.000000")


if __name__ == "__main__":
    unittest.main()
