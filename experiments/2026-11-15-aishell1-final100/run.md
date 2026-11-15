# AISHELL-1 Final-100 Decoding Confirmation

## Status

Completed. Only aggregate metrics were inspected for this batch; no per-utterance error analysis was used to change the selected decoding strategy.

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

## Aggregate Results

| Mode | CER | N | C | S | D | I | Audio seconds | Wall-clock seconds | RTF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `ctc_greedy_search` | 6.47% | 1469 | 1375 | 91 | 3 | 1 | 516.006749 | 6.193562 | 0.012003 |
| `attention_rescoring` | 6.06% | 1469 | 1380 | 86 | 3 | 0 | 516.006749 | 28.814710 | 0.055842 |

- Both conditions produced 100 predictions for 100 inputs.
- Attention rescoring reduced CER by 0.41 percentage points, with five fewer substitutions and one fewer insertion than greedy search.
- Attention rescoring required 4.65 times the greedy wall-clock time in this run.

## Confirmation

The B-selected `attention_rescoring` strategy also has the lower CER on this independent C batch. This is an in-domain result for this fixed AISHELL-1 protocol and checkpoint only; it is not a generalization claim. The decoding selection remains frozen after this confirmation. No additional mode selection or parameter tuning will use this batch.
