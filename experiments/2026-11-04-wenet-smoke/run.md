# WeNet AISHELL-1 Smoke Test

## Status

Template only. No checkpoint has been downloaded and no inference result has been produced yet.

## Purpose

Run the official WeNet recognizer on five Mandarin WAV clips as an execution qualification test. Personal clips are smoke-test inputs only and must not be used to report CER.

## Candidate artifacts

- WeNet repository: `https://github.com/wenet-e2e/wenet.git`
- WeNet commit: `be6ad97fdb512589df113042f7ff3a29d392fb38`
- Checkpoint source: official AISHELL entry in `third_party/wenet/docs/pretrained_models.md`
- Dataset source and license: AISHELL-1, OpenSLR SLR33, Apache License 2.0
- Checkpoint SHA-256: record after download

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
