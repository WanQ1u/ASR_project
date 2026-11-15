# AISHELL-1 Final-100 Decoding Confirmation

## Status

Completed. Aggregate metrics and a descriptive text-level per-utterance error analysis were inspected. Neither was used to change the selected decoding strategy.

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

## Text-Level Error Analysis

This is a descriptive analysis of the final selected system, not evidence for an acoustic or language-model causal claim. No C-batch audio was listened to for this pass.

- Exact predictions: 57 / 100 utterances.
- Utterances with at least one character error: 43 / 100.
- Character errors: 89 total = 86 substitutions + 3 deletions + 0 insertions.
- Six utterances with CER at least 30% contain 27 of the 89 character errors (30.3%).

The 43 incorrect utterances were manually assigned one primary text-level pattern. Categories are not causal diagnoses and individual utterances can contain more than one pattern.

| Primary pattern | Utterances | Representative examples |
| --- | ---: | --- |
| Proper names, place names, or other rare named strings | 10 | `钟晶晶` -> `钟京京`; `封丘县留光镇` -> `中秋县刘光镇`; `潘玮柏` -> `潘玮博` |
| Single-character or short-phrase alternatives consistent with homophone or near-homophone confusion | 22 | `似是而非` -> `四事而非`; `跑输` -> `跑出`; `西红柿` -> `西红式` |
| Rare or domain-specific multi-character phrases | 8 | `美初裁中国产轮胎倾销` -> `每出台中国产轮胎七星`; `测土配方施肥` -> `侧土配方师肥`; `退牧还草` -> `退木管草` |
| Deletion of a short segment | 3 | `商住用地` -> `商住地`; `她本人` -> `她本`; `内地产投资` -> `内地投资` |

Compared with greedy, attention rescoring reduces total C-batch errors from 95 to 89. Its improvements are local corrections such as `站例` -> `站立`, `我爱五家` -> `我爱我家`, `实力调查` -> `实地调查`, and `再迎` -> `再也`; the highest-error rare-name and rare-phrase cases remain unresolved. Because this analysis now informs subsequent work, C must not be reused as the final blind test for a later changed system.
