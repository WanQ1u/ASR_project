# AISHELL-1 Official Test-100 Development Baseline

## Status

Data download and deterministic subset preparation are complete. No AISHELL-1 prediction or CER has been inspected.

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
- Archive SHA-256: `a4a0313cde0a933e0e01a451f77de0a23d6c942f4694af5bb7f40b9dc38143fe`
- Downloaded on Windows at `C:\\Users\\32112\\Downloads\\data_aishell.tgz`.
- Official test candidates inspected: 7,176 utterances.
- Frozen subset manifest: `subset.tsv`, exactly 100 utterances selected with seed `20261109`.
- Selected WAV transfer bundle SHA-256: `b75de95ac62e701036dc2ecdb5cbca16c3df1b13034d867945f614d177bb264b`.
- Selected WAVs and transcript were transferred to Linux and verified before inference.
- Linux extracted data root: `/home/qwh/ASR_project/data/aishell1/extracted-test100/data_aishell`.
- Extraction verification:
- WeNet commit: `be6ad97fdb512589df113042f7ff3a29d392fb38`
- Checkpoint SHA-256: `f368e24e6c84aaf770ffa36e6973596274de5288810315f9b9c5f4f4037fe16d`
- Exact command:
- Start / end time:
- GPU / runtime:
- Prediction coverage:
- Prediction coverage: 100 / 100
- CER (S / D / I / N): 4.27% (S=63, D=1, I=0, N=1499, C=1435)
- Total audio duration: 505.144813 seconds
- Wall-clock duration: 24.204622 seconds
- RTF: 0.047916
- Repeat prediction match: exact match between `baseline-run-1` and `baseline-run-2` prediction files.

## Preliminary Error Analysis

- 69/100 utterances have zero character errors; 31/100 have at least one error.
- Aggregate errors are substitutions only, except for one deletion: S=63, D=1, I=0. There are no insertion errors.
- Frequent patterns are homophone or near-homophone substitutions (for example `宋芳` -> `宋方`, `累积` -> `累计`, `谢霆锋` -> `谢霆峰`), proper names and place names (for example `马塞洛`, `渤海`, `苍南县`, `桃太郎`), and low-frequency names or long sequences.
- The highest-utterance error rates are concentrated in rare-name or long-sequence examples, including `一百一十米栏...`, `她几乎担当起了...`, and `在冈山的桃太郎体育馆`.
- This is a text-level diagnosis from reference/hypothesis alignment. It does not by itself distinguish acoustic confusion from language-model or vocabulary effects; audio inspection would be required for that claim.
