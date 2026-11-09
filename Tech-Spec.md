# Mandarin ASR Baseline Technical Specification

## Status

Active. Created 2026-11-04.

## Baseline Candidate

- Repository: `wenet-e2e/wenet`.
- Candidate checkpoint: AISHELL-1 U2++ Conformer checkpoint model from the official WeNet pretrained-model page.
- Candidate evaluation corpus: AISHELL-1 (OpenSLR SLR33), Apache License 2.0.
- Runtime: Python on the existing Linux GPU server; CPU is permitted only for a smoke test.

## Reproducibility Contract

Each experiment must create a dated directory under `experiments/` containing:

- `run.md`: command, UTC start/end, hardware, Git commit, package versions, model artifact URL and SHA-256.
- `inputs.tsv`: relative audio path, duration, and source category (`personal-smoke` or `public-eval`).
- `predictions.tsv`: audio path, prediction, and any runtime error.
- `environment.txt`: `python --version`, `pip freeze`, `nvidia-smi`, and `git rev-parse HEAD` output.

Never save credentials, private recordings, or absolute home-directory paths in these artifacts.

The project Git repository tracks source, manifests, run records, and checksums only. It excludes upstream checkouts, model weights, audio, logs, and machine-specific environment dumps.

## Data Protocol

- Personal recordings are smoke-test inputs only and are excluded from CER reporting.
- Before Week 2, one public AISHELL-1 subset and its manifest are frozen in version control.
- The current development subset contains exactly 100 utterances from the official AISHELL-1 `test` split. Candidate utterance IDs are sorted lexicographically, then sampled without replacement with Python `random.Random(20261109)`. The resulting IDs and references are committed before inference.
- The official AISHELL-1 test split is never used to choose a model, decoding setting, or training hyperparameter.
- Any direct overlap between checkpoint training data and a reported evaluation set is explicitly labelled as in-domain benchmark evaluation.

## Metrics

- Week 1: inference success rate and wall-clock duration only.
- Week 2 onward: character error rate (CER), substitutions, deletions, insertions, and representative errors.
- For every public evaluation run, record total audio duration, wall-clock decoding duration, and RTF (`wall-clock seconds / total audio seconds`).

## Verification

- Confirm the official command runs twice on the same audio without runtime failure.
- Confirm every saved prediction corresponds to one input row.
- Verify checksums after every model download.
