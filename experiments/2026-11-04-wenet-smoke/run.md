# WeNet AISHELL-1 Smoke Test

## Status

Passed on 2026-11-09: the official WeNet recognizer produced one non-empty transcript for each of the five personal smoke-test WAV clips.

## Purpose

Run the official WeNet recognizer on five Mandarin WAV clips as an execution qualification test. Personal clips are smoke-test inputs only and must not be used to report CER.

## Candidate artifacts

- WeNet repository: `https://github.com/wenet-e2e/wenet.git`
- WeNet commit: `be6ad97fdb512589df113042f7ff3a29d392fb38`
- Checkpoint source: official AISHELL entry in `third_party/wenet/docs/pretrained_models.md`
- Dataset source and license: AISHELL-1, OpenSLR SLR33, Apache License 2.0
- Checkpoint archive: `aishell_u2pp_conformer_exp.tar.gz`
- Archive SHA-256: `52e0f792ffc2806a2739a9920170ad8eb899bf25e192eefa60109a9eec82d344`
- Archive member checkpoint: `20210601_u2++_conformer_exp_aishell/final.pt`
- Extracted checkpoint SHA-256: `f368e24e6c84aaf770ffa36e6973596274de5288810315f9b9c5f4f4037fe16d`

## Runtime record

- Start time: 2026-11-09 21:50:00 (server-local log timestamp)
- Host: `labserver-System`
- GPU: NVIDIA GeForce RTX 3090 (`--gpu 0`)
- Python / PyTorch / CUDA: Python 3.10.22 / PyTorch 2.9.1+cu128 / CUDA runtime 12.8
- Audio loader dependencies: TorchCodec 0.9.0 and FFmpeg 7.1 in `/home/qwh/ASR_project/.conda`
- Command: `scripts/run_wenet_smoke.py` with the fixed paths in the project README and the five-row `inputs.tsv` manifest
- Checkpoint path: `models/20210601_u2++_conformer_exp_aishell/final.pt`
- Checkpoint SHA-256: `f368e24e6c84aaf770ffa36e6973596274de5288810315f9b9c5f4f4037fe16d`
- Inference success count: 5 / 5 non-empty CTC greedy-search transcripts
- Repeat transcript match: not yet checked

The raw audio, runtime logs, and personal transcripts remain on the Linux server and are not committed to Git.

## Interpretation

Passing this smoke test qualifies the tooling for the next fixed-subset evaluation step. It does not establish generalization quality.
