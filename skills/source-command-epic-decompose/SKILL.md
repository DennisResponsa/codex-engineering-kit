---
name: source-command-epic-decompose
description: Break an epic into task children without creating task branches.
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

# /epic-decompose

Reconcile the task breakdown for one epic issue.

```bash
node scripts/github-coordination.js decompose <issue-number> --repo <owner/repo>
```

What this does:

1. Reads the epic issue body for task checklists and dependency references.
2. Stores the decomposition in the coordination block.
3. Leaves task branches out of the workflow.
4. Appends a concise audit comment.

Compatibility aliases:

- `/plan`
- `/prp-plan`
