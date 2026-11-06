---
name: orch-change-feature
description: Orchestrate altering an existing, working feature to new desired behavior
  — update its tests to the new spec, change the implementation to match, review,
  and gated commit. Use when behavior is not broken but should be different.
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

# orch-change-feature

Actor · action · target: **orch · change · feature**. Thin wrapper over the
shared engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

## When to Use

- An existing feature **works**, but the desired behavior is different ("change",
  "adjust", "make it also …", "instead of X do Y").
- Distinguish from siblings:
  - **not** broken → not `orch-fix-defect` (no bug to reproduce).
  - **not** new → not `orch-add-feature` (the capability already exists).

## Operation settings

- **Default size floor:** small — most tweaks are a function or two.
- **Phase mask:** 0 → (1 only if the new behavior needs research) → light 2 →
  4 → 5 → 6.
- **First move (phase 4):** update the *existing* tests to express the new
  desired behavior, then change the implementation until they pass. Changing the
  tests first is what separates a tweak from a fix.

## How It Works

1. Run the `orch-pipeline` engine with the settings above.
2. Keep the plan light — only `standard`+ size warrants the full `planner` pass.
3. Stop at **Gate 1** (plan / changed-test approval) and **Gate 2** (pre-commit).
4. Add `security-reviewer` if the change touches a security trigger.

## Example

```
orch-change-feature: make nws-poller alert at 2 warnings instead of 3
→ update threshold tests to new spec → change impl to green
→ code-review → commit  [GATE 2: confirm]
```
