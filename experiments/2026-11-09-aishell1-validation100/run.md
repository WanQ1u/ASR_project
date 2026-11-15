# AISHELL-1 Validation-100 Decoding Comparison

## Status

Prepared and transferred. No prediction, CER, or per-utterance error has been inspected for this batch.

## Role

This is the B validation batch for selecting one decoding strategy. It is disjoint from the earlier A development/error-analysis batch.

## Frozen Selection Policy

- Corpus: AISHELL-1 official `test` split only.
- Candidate pool: the 7,176 official test utterances available in the downloaded speaker archives, excluding all 100 A-batch utterances.
- Remaining candidates: 7,076.
- Selection: sort remaining utterance IDs lexicographically, then sample without replacement with Python `random.Random(20261115)`.
- Subset size: exactly 100 utterances.
- Overlap with A batch: zero.
- Do not replace entries after inspecting decoding results.

## Artifacts

- Manifest: `subset.tsv`
- Linux data root: `/home/qwh/ASR_project/data/aishell1/extracted-validation100/data_aishell`
- Uploaded bundle SHA-256: `7f0d2ce46f0e19ab49322ed7133f9415a44e0b27d61dc510234739872b693466`
- Manifest SHA-256: `cda302c9eb9de36017ad66916f1c812c5a5d50af479b488f0e904a5f6343a086`

## Evaluation Protocol

Run the same 100 utterances with `ctc_greedy_search`, `ctc_prefix_beam_search`, and `attention_rescoring`. Compare CER, S/D/I, wall-clock duration, and RTF before selecting one strategy. No C final-test batch is selected or evaluated until this choice is frozen.
