# Mandarin ASR Baseline

This project reproduces and evaluates a pretrained Mandarin automatic speech recognition (ASR) model before any fine-tuning or unlearning work.

## Current baseline candidate

- Toolkit: WeNet
- Dataset associated with the checkpoint: AISHELL-1
- Model: AISHELL U2++ Conformer checkpoint
- WeNet commit: `be6ad97fdb512589df113042f7ff3a29d392fb38`
- Runtime host: Linux GPU server
- Development host: Windows

The candidate is provisional until the official inference path succeeds on five smoke-test clips and the repository, checkpoint, and environment are recorded.

## Repository layout

- `third_party/wenet/`: local upstream checkout; ignored by Git
- `scripts/`: project-owned wrappers that call the upstream inference entry point
- `experiments/`: dated manifests and run records
- `PRD.md`: research scope and acceptance criteria
- `Tech-Spec.md`: reproducibility and data protocol

## Development and execution workflow

1. Edit code and documentation on Windows.
2. Commit and push the project metadata to GitHub.
3. Pull the commit on Linux.
4. Install and use the Linux GPU environment, download model artifacts, and run experiments there.
5. Commit only reproducible metadata and result summaries; keep environments, audio, model weights, and logs ignored.

## Smoke-test entry point

The wrapper in `scripts/run_wenet_smoke.py` prepares the JSONL input expected by WeNet and invokes the official `wenet/bin/recognize.py`. It does not modify the upstream checkout or implement a second ASR decoder.

The exact checkpoint path, config path, and audio manifest are supplied at runtime on Linux after the official checkpoint archive has been inspected.

## Evidence sources

- WeNet pretrained model list: `third_party/wenet/docs/pretrained_models.md`
- Official AISHELL recipe and decoding command: `third_party/wenet/examples/aishell/s0/run.sh`
- Official recognizer input and arguments: `third_party/wenet/wenet/bin/recognize.py`
- Project acceptance criteria: `PRD.md`, `Tech-Spec.md`, and `docs/superpowers/plans/`
