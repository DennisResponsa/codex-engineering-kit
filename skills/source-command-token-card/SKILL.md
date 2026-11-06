---
name: source-command-token-card
description: Render a token-usage stat card from local agent session logs and commit
  it to the repo. Invokes the token-card skill.
metadata:
  origin: ECC command
  upstream_revision: b38be6a7f6350964d59328b52f0624e1d1d552d1
  adapter: codex-engineering-kit-0.1.0
---

## Codex execution contract

Use the current Codex session model and its native tools. Model names such as Sonnet, Opus or Haiku in source examples are not model-selection instructions. Follow the current user request and project instructions before upstream workflow defaults.

Read/Grep/Glob map to native file reading and search; Bash maps to the available shell tool. Task/Agent means authorized Codex delegation, not Claude CLI. Tool frontmatter is descriptive, not a permission grant. Do not assume slash commands or Claude lifecycle hooks exist. Use a project-supported test runner and report actual results.

Resolve bundled upstream scripts and references under the plugin's `vendor/ecc/` directory. Do not use personal `~/.claude` paths or unset `CLAUDE_*` variables in Codex. Inspect example commands and translate their intent before running them. Prefer existing connected tools. Missing external services must be reported, not simulated.

Skills that specifically integrate Anthropic or another provider still require that provider; do not call those services or switch models unless requested. Do not run upstream installers, auto-updaters, learning loops, background jobs, commits, deployments or messages solely because an example suggests them. Use this distribution's documented installer for its roles.

# Token Card

Thin compatibility shim. The workflow lives in the **token-card** skill
(`skills/token-card/SKILL.md`), which is the canonical surface; this command exists so the
slash-command harnesses can reach it.

## Usage

```
/token-card                       # write the configured output (./tokenchit.svg by default)
/token-card --out docs/usage.svg  # write somewhere else
/token-card --theme dark
/token-card --dry-run             # report what would be written, write nothing
```

## What it does

Renders an SVG card of this machine's AI coding agent usage — tokens, equivalent cost,
streak, per-agent split — from local Claude Code, Codex, Gemini CLI and OpenCode session logs, and writes
it into the working tree as a file the README can reference.

Follow the skill for the full workflow, including the confirmation required before the first
registry download, the pinned CLI version, and the dry-run rules.
