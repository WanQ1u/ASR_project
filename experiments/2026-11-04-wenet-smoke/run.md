# WeNet AISHELL-1 Smoke Test

## Status

Checkpoint archive has been downloaded locally, but it has not yet been transferred to Linux or used for inference. No inference result has been produced yet.

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
- Extracted checkpoint SHA-256: record on Linux after transfer and extraction

## Runtime record

Fill this section on Linux after the run:

- Start time (UTC):
- End time (UTC):
- Host:
- GPU:
- Python / PyTorch / CUDA:
- Exact command:
- Checkpoint path:
- Checkpoint SHA-256:
- Inference success count:
- Repeat transcript match:

## Interpretation

Passing this smoke test qualifies the tooling for the next fixed-subset evaluation step. It does not establish generalization quality.
