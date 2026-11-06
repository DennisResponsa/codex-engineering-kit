---
name: source-command-hookify-help
description: Get help with the hookify system
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

Display comprehensive hookify documentation.

## Hook System Overview

Hookify creates rule files that integrate with Claude Code's hook system to prevent unwanted behaviors.
ECC's built-in runtime loads these rules automatically while plugin hooks are
enabled; installing a separate Hookify plugin is not required.

### Event Types

- `bash`: triggers on Bash tool use and matches command patterns
- `file`: triggers on Write/Edit tool use and matches file paths
- `stop`: triggers after each Claude response
- `prompt`: triggers on user message submission and matches input patterns
- `all`: triggers on all events

### Rule File Format

Files are stored as `.claude/hookify.{name}.local.md`:

```yaml
---
name: descriptive-name
enabled: true
event: bash|file|stop|prompt|all
action: block|warn
pattern: "regex pattern to match"
---
Message to display when rule triggers.
Supports multiple lines.
```

### Commands

- `/hookify [description]` creates new rules and auto-analyzes the conversation when no description is given
- `/hookify-list` lists configured rules
- `/hookify-configure` toggles rules on or off

### Pattern Tips

- use regex syntax
- for `bash`, match against the full command string
- for `file`, match against the file path
- test patterns before deploying
- avoid nested quantifiers such as `(a+)+`; the runtime rejects unsafe regexes
- every regex evaluation also has a 25 ms hard timeout
- malformed or oversized rules fail open with a diagnostic so one bad local rule cannot disable all hooks
- Git-tracked local rules require explicit `ECC_HOOKIFY_ALLOW_TRACKED=1` approval

### Action Behavior

- `warn` adds the rule message to Claude's context and allows processing to continue
- `block` denies matching shell/file actions before execution
- `block` on prompt, post-tool, or stop events uses that event's structured block decision
- stop rules are skipped when `stop_hook_active` is already true to prevent loops
