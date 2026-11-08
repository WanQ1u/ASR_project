# Mandarin ASR Baseline Reproduction PRD

## Status

Active. Created 2026-11-04.

## Problem

The project needs a credible, reproducible starting point for evaluating a pretrained Mandarin ASR model before any fine-tuning or machine-unlearning claim is considered.

## Research Question

Can a public Mandarin ASR checkpoint be reproduced with its documented inference path and evaluated on a fixed, license-compatible public test split?

## Initial Decision

Use the WeNet repository and its AISHELL-1 U2++ Conformer checkpoint as the primary baseline candidate. This is a provisional execution decision: it becomes the project baseline only after its official inference path succeeds and the repository commit, checkpoint artifact, and environment are recorded. AISHELL-1 is the candidate evaluation corpus because it provides Mandarin speech, transcripts, speaker metadata, and an Apache-2.0 license.

## Scope

- Run official checkpoint inference on five Mandarin WAV clips.
- Record exact repository commit, checkpoint checksum, Python/PyTorch/CUDA versions, hardware, commands, duration, and transcripts.
- Prepare, but do not yet tune on, an AISHELL-1 evaluation subset.

## Non-goals

- No training, fine-tuning, hyperparameter search, or unlearning experiment this week.
- No quality claim based on personal recordings.
- No use of the fixed test split for tuning.

## Acceptance Criteria

- Five input files produce saved transcripts through one documented command or script.
- A run record identifies every artifact needed to repeat the inference run.
- The selected checkpoint's provenance and applicable dataset/model license are recorded.
- The plan for the next week fixes an evaluation subset without using its results to alter this week's inference configuration.

## Risks

- Checkpoint download, CUDA, or dependency incompatibility can block inference.
- A checkpoint trained on AISHELL-1 must be reported as an in-domain benchmark baseline, not as an unseen-domain generalization result.
- Model-weight terms must be checked independently from repository terms.
