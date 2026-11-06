---
name: orch-add-feature
description: Orchestrate building a brand-new feature end to end — research, plan,
  TDD implementation, review, and gated commit — by delegating each phase to the matching
  ECC agent. Use when adding a capability that does not exist yet.
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

# orch-add-feature

Actor · action · target: **orch · add · feature**. Thin wrapper over the shared
engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

## When to Use

- The user wants a capability that does **not exist yet** ("add", "build",
  "implement", "support …").
- It is net-new behavior — not a correction (`orch-fix-defect`) and not an
  alteration of existing behavior (`orch-change-feature`).

## Operation settings

- **Default size floor:** standard — run Research + Plan unless clearly small.
- **Phase mask:** 0 → 1 → 2 → 4 → 5 → 6 (skip 3 Scaffold; that is MVP-only).
- **First move (phase 4):** write *new* failing tests for the new behavior, then
  implement to green.

## How It Works

1. Run the `orch-pipeline` engine with the settings above.
2. Classify size first; small / trivial features collapse toward 4 → 5 → 6.
3. Stop at **Gate 1** (plan approval) and **Gate 2** (pre-commit).
4. Add `security-reviewer` if the feature touches a security trigger.

> Related: `/feature-dev` is a standalone version of this flow. `orch-add-feature`
> differs by sharing the `orch-pipeline` engine — the size classifier and the two
> gates — with the rest of the family, so it right-sizes trivial features to 4 → 5 → 6.

## Example

```
orch-add-feature: add OAuth2 login to nws-poller
→ research existing auth libs → plan task_list  [GATE 1: approve]
→ TDD each task → code-review (+ security-reviewer: auth path)
→ commit  [GATE 2: confirm]
```
