# Training Qualification Validation Plan

## Goal

Verify that the local WeNet AISHELL-1 training loop can load data, run a forward pass, compute loss, perform backpropagation, save a checkpoint, and evaluate a development set. This is an engineering qualification check, not a formal ASR result and not a machine-unlearning experiment.

## Fixed decisions

- Code and documentation are maintained on Windows and synchronized through GitHub.
- Linux is used for data preparation, GPU training, and runtime outputs.
- The official WeNet AISHELL recipe and `train_u2++_conformer.yaml` are the reference configuration.
- The downloaded pretrained `final.pt` is not overwritten and is not used as the formal machine-unlearning starting point.
- Training artifacts, full audio, manifests generated on Linux, logs, and environments remain outside Git.

## Qualification protocol

1. Transfer the verified Windows `data_aishell.tgz` archive to Linux and verify its SHA-256 before extraction.
2. Extract the official AISHELL-1 corpus under the ignored Linux data directory.
3. Run the official AISHELL data-preparation stages to produce `train`, `dev`, and `test` manifests, CMVN, and a character dictionary.
4. Create a small qualification-only train/dev manifest from the official manifests. This subset is only for checking the training code path; it is not an evaluation set and will not be used for research claims.
5. Run WeNet training for one short epoch with a new model directory under `experiments/`, overriding paths and `max_epoch` without changing the downloaded checkpoint.
6. Confirm that an epoch checkpoint, `final.pt` symlink, training log, and development loss are produced.

## Acceptance criteria

- Data preparation exits successfully.
- At least one training epoch completes without a data-loader, CUDA, loss, or distributed-training error.
- A new checkpoint is written outside `models/20210601_u2++_conformer_exp_aishell/`.
- A development loss is recorded for the same run.
- The original pretrained checkpoint checksum and files are unchanged.

## Follow-up

After this qualification passes, decide the formal training protocol and speaker split for `M_all`, `M_retrain`, and the machine-unlearning baseline. Do not infer model quality from the short qualification run.
