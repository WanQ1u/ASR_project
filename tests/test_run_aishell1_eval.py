import csv
import tempfile
import unittest
from pathlib import Path

from scripts.run_aishell1_eval import build_recognize_command, load_subset


class RunAishell1EvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.audio = self.root / "data" / "data_aishell" / "wav" / "test" / "S0001" / "BAC001.wav"
        self.audio.parent.mkdir(parents=True)
        self.audio.write_bytes(b"RIFF")
        self.subset = self.root / "subset.tsv"
        with self.subset.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["utterance_id", "audio_path", "reference_text", "duration_seconds", "source_split"], delimiter=chr(9))
            writer.writeheader()
            writer.writerow({"utterance_id": "BAC001", "audio_path": "data/data_aishell/wav/test/S0001/BAC001.wav", "reference_text": "测试文本", "duration_seconds": "1.000000", "source_split": "aishell1-test"})

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_load_subset_resolves_audio_and_preserves_reference(self) -> None:
        records = load_subset(self.subset, self.root)

        self.assertEqual(records[0].utterance_id, "BAC001")
        self.assertEqual(records[0].audio_path, self.audio.resolve())
        self.assertEqual(records[0].reference_text, "测试文本")

    def test_build_recognize_command_overrides_checkpoint_artifact_paths(self) -> None:
        model_dir = self.root / "models" / "checkpoint"
        command = build_recognize_command(
            python=Path("/venv/bin/python"),
            wenet_root=self.root / "third_party" / "wenet",
            config=model_dir / "train.yaml",
            checkpoint=model_dir / "final.pt",
            data_list=self.root / "logs" / "data.list",
            result_dir=self.root / "logs",
            gpu=0,
        )

        self.assertIn("tokenizer_conf.symbol_table_path " + str(model_dir / "units.txt"), command)
        self.assertIn("cmvn_conf.cmvn_file " + str(model_dir / "global_cmvn"), command)
        self.assertEqual(command[0], str(Path("/venv/bin/python")))


if __name__ == "__main__":
    unittest.main()
