---
name: orch-refine-code
description: Orchestrate a behavior-preserving refactor — confirm tests are green,
  restructure without changing behavior, keep tests green, review, and gated commit.
  Use when the structure should improve but behavior must not change.
metadata:
  origin: ECC
  upstream_revision: b38be6a7f6350964d59328b52f0624e1d1d552d1
  adapter: codex-engineering-kit-0.1.0
---

## Codex execution contract

Use the current Codex session model and its native tools. Model names such as Sonnet, Opus or Haiku in source examples are not model-selection instructions. Follow the current user request and project instructions before upstream workflow defaults.

Read/Grep/Glob map to native file reading and search; Bash maps to the available shell tool. Task/Agent means authorized Codex delegation, not Claude CLI. Tool frontmatter is descriptive, not a permission grant. Do not assume slash commands or Claude lifecycle hooks exist. Use a project-supported test runner and report actual results.

Resolve bundled upstream scripts and references under the plugin's `vendor/ecc/` directory. Do not use personal `~/.claude` paths or unset `CLAUDE_*` variables in Codex. Inspect example commands and translate their intent before running them. Prefer existing connected tools. Missing external services must be reported, not simulated.

Skills that specifically integrate Anthropic or another provider still require that provider; do not call those services or switch models unless requested. Do not run upstream installers, auto-updaters, learning loops, background jobs, commits, deployments or messages solely because an example suggests them. Use this distribution's documented installer for its roles.

# orch-refine-code

Actor · action · target: **orch · refine · code**. Thin wrapper over the shared
engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

## When to Use

- Same behavior, **better structure**: extract modules, remove duplication, kill
  dead code, reduce nesting, rename for clarity.
- Distinguish from siblings: if behavior is meant to change at all, this is the
  wrong skill (`orch-change-feature` / `orch-fix-defect`).

## Operation settings

- **Default size floor:** standard — restructures touch multiple files.
- **Phase mask:** 0 → 2 (plan the restructure) → 4 (keep green) → 5 → 6. No new
  behavior tests are written — the existing suite is the safety net.
- **First move (phase 4):** confirm the relevant tests exist and are **green
  before** touching code; if coverage is thin, add characterization tests first.
  Then restructure in small steps, re-running tests after each.

## How It Works

1. Run the `orch-pipeline` engine with the settings above.
2. For dead-code / duplication sweeps, delegate to the `refactor-cleaner` agent
   (it runs knip / depcheck / ts-prune and removes safely).
3. Stop at **Gate 1** (restructure plan) and **Gate 2** (pre-commit).
4. Commit as `refactor:` — the diff must be behavior-neutral.

## Example

```
orch-refine-code: extract the NWS HTTP client out of poller.py
→ confirm tests green → plan extraction  [GATE 1: approve]
→ move in small steps, tests green throughout → code-review
→ commit refactor:  [GATE 2: confirm]
```
