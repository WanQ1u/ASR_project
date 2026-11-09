# AISHELL-1 Official Test-100 Development Baseline

## Status

Data download and deterministic subset preparation are in progress. No AISHELL-1 prediction or CER has been inspected.

## Frozen Evaluation Policy

- Corpus: AISHELL-1, OpenSLR SLR33, Apache-2.0.
- Source split: official `test` split only.
- Subset size: 100 utterances.
- Selection: sort all eligible utterance IDs lexicographically, then sample without replacement using Python `random.Random(20261109)`.
- Membership rule: never replace an utterance after inspecting a prediction, error, runtime, or CER.
- Interpretation: this is an in-domain development baseline for workflow validation, not a final full-test result or a generalization claim.

## Runtime Record

- Dataset archive URL: `http://www.openslr.org/resources/33/data_aishell.tgz`
- Dataset archive size: 15,582,913,665 bytes
- Archive SHA-256:
- Extraction verification:
- WeNet commit: `be6ad97fdb512589df113042f7ff3a29d392fb38`
- Checkpoint SHA-256: `f368e24e6c84aaf770ffa36e6973596274de5288810315f9b9c5f4f4037fe16d`
- Exact command:
- Start / end time:
- GPU / runtime:
- Prediction coverage:
- CER (S / D / I / N):
- Total audio duration:
- Wall-clock duration:
- RTF:
- Repeat prediction match:
