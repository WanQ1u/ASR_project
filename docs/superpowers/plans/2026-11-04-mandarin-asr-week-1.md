# Mandarin ASR Week 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a repeatable five-file Mandarin ASR inference run using the official WeNet AISHELL-1 checkpoint path.

**Architecture:** Keep the upstream WeNet checkout unmodified. Store commands and outputs in a dated experiment directory so the smoke test is separate from the later fixed public evaluation.

**Tech Stack:** Python, PyTorch, WeNet, Linux, NVIDIA CUDA where available.

## Global Constraints

- Do not train, fine-tune, or tune decoding settings during this plan.
- Treat personal audio as smoke-test data only.
- Pin the repository commit, model artifact checksum, and package versions before reporting a result.
- Do not record secrets or private absolute paths.

---

### Task 1: Pin baseline artifacts

**Files:**
- Create: `experiments/2026-11-04-wenet-smoke/run.md`
- Create: `experiments/2026-11-04-wenet-smoke/environment.txt`

- [ ] Initialize the project Git repository if `git status` reports no repository; track metadata only and ignore `third_party/`, model weights, audio, logs, and environment dumps.
- [ ] Clone `https://github.com/wenet-e2e/wenet.git` into `third_party/wenet` and save `git -C third_party/wenet rev-parse HEAD`.
- [ ] Save `python --version`, `python -m pip freeze`, `nvidia-smi`, and that Git commit to `environment.txt`.
- [ ] Record the official checkpoint URL and AISHELL-1 license URL in `run.md`; download the checkpoint and record `sha256sum` output there.

### Task 2: Execute a five-clip smoke test

**Files:**
- Create: `experiments/2026-11-04-wenet-smoke/inputs.tsv`
- Create: `experiments/2026-11-04-wenet-smoke/predictions.tsv`

- [ ] Add five 16 kHz mono Mandarin WAV paths to `inputs.tsv`, with header `audio_path\tduration_seconds\tsource_category` and `personal-smoke` as every source category.
- [ ] Run the unmodified official checkpoint inference path for every manifest row, retaining stdout and stderr under the experiment directory.
- [ ] Create one `predictions.tsv` row per input with header `audio_path\tprediction\tstatus\terror`; require five non-empty predictions and five `success` statuses.
- [ ] Repeat the first command unchanged and record whether normalized transcript text matches plus both durations.

### Task 3: Apply the qualification gate

**Files:**
- Modify: `experiments/2026-11-04-wenet-smoke/run.md`
- Modify: `MEMORY.md`

- [ ] Pass only when all five transcripts are non-empty, all manifest paths match output paths, and the repeat transcript is identical.
- [ ] If passed, update `MEMORY.md` to record WeNet AISHELL-1 U2++ Conformer as selected baseline and schedule a fixed-subset CER evaluation; otherwise document the exact failing command and error before changing candidates.
- [ ] Commit metadata only with `git add PRD.md Tech-Spec.md MEMORY.md docs/superpowers/plans/2026-11-04-mandarin-asr-week-1.md experiments/2026-11-04-wenet-smoke` and `git commit -m "docs: plan Mandarin ASR baseline smoke test"`.

## Self-Review

- Spec coverage: Tasks 1–3 cover all PRD acceptance criteria.
- Placeholder scan: no `TBD`, `TODO`, or deferred implementation instruction appears.
- Interface consistency: Task 1 supplies artifacts for Task 2; Task 2 supplies evidence for Task 3.
