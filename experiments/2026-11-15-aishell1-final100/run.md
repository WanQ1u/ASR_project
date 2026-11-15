# AISHELL-1 Final-100 Decoding Confirmation

## Status

Prepared and transferred. No prediction, CER, or per-utterance error has been inspected for this batch.

## Role

This is the C final-confirmation batch. It is reserved for one comparison between the original `ctc_greedy_search` baseline and the B-selected `attention_rescoring` strategy.

## Frozen Selection Policy

- Corpus: AISHELL-1 official `test` split only.
- Candidate pool: the 7,176 official test utterances available in the downloaded speaker archives, excluding all 100 A-batch utterances and all 100 B-batch utterances.
- Remaining candidates: 6,976.
- Selection: sort remaining utterance IDs lexicographically, then sample without replacement with Python `random.Random(20261116)`.
- Subset size: exactly 100 utterances.
- Overlap with A batch: zero.
- Overlap with B batch: zero.
- Do not replace entries or select another decoding method after inspecting this batch.

## Artifacts

- Manifest: `subset.tsv`
- Linux data root: `/home/qwh/ASR_project/data/aishell1/extracted-final100/data_aishell`
- Uploaded bundle SHA-256: `95b0a1692d1a0b899270281db6c81cac77b840311f437b0212e4f4bfe3cb2e7e`
- Manifest SHA-256: `f6bd004f8015a60a4d96842daf3d9ca4c4deeb2294bc67effcaed3d91cf85695`

## Evaluation Protocol

Run exactly two conditions on the same 100 utterances: `ctc_greedy_search` and `attention_rescoring`. Record prediction coverage, CER, S/D/I, total audio duration, wall-clock duration, and RTF. This batch is for confirmation only; do not use its aggregate or per-utterance results to change the selected decoding strategy.
