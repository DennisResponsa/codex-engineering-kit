---
name: deepseek-harness-setup
description: 'Install and operate Everything Codex (ECC) on the DeepSeek Harness (DSH):
  native skill roots (~/.dsh/skills, .agents/skills), the @deepseek-ai/dsh-hooks-claude-code
  bridge for command hooks, bare-insert patch mounting, generator usage, event-support
  limits, and update workflow. Use when setting up ECC on DeepSeek Harness, wiring
  ECC hooks into a DSH profile, or debugging why ECC skills or hooks do not appear
  in a DSH session.'
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

# DeepSeek Harness Setup

Run ECC on the DeepSeek Harness. Full guide: `docs/DEEPSEEK-HARNESS-GUIDE.md`.

## When to Use

- Installing ECC skills or hooks on a DeepSeek Harness install.
- Deciding which ECC surfaces work on DSH and which do not.
- Debugging a DSH session that does not show ECC skills or does not fire ECC hooks.

## How It Works

1. **Skills need no conversion.** DSH reads `SKILL.md` frontmatter
   (name/description) from native skill roots. Link the ECC catalog once:

   ```bash
   ln -s /path/to/ECC/skills/<skill-name> ~/.dsh/skills/<skill-name>
   ```

   Root priority (project `.dsh` and `.agents` roots beat `~/.dsh`): skip
   linking skills whose names already exist in a higher-priority root.
   Substitute real skill names for the placeholders; the angle brackets are
   not shell syntax.

2. **Hooks go through the first-party bridge.** Generate a DSH-format config
   from the canonical ECC hooks file:

   ```bash
   node scripts/dsh/generate-hooks-config.js --ecc-root /path/to/ECC --out ~/.dsh/ecc/hooks-dsh.json
   ```

   The generator lower-cases tool-name matchers, prefixes
   `CLAUDE_PLUGIN_ROOT`/`ECC_PLUGIN_ROOT` inline (the bridge does not export
   the plugin root), preserves timeouts, and skips events DSH cannot bridge:
   `PreCompact`, `PostToolUseFailure`, `SessionEnd`.

3. **Mount with a bare insert** in `~/.dsh/profiles/<profile>/cordis.patch.yml`:

   ```yaml
   - insert:
       - id: ecc-hooks-claude-code
         name: "@deepseek-ai/dsh-hooks-claude-code"
         config:
           configPath: /absolute/path/to/hooks-dsh.json
   ```

   Loader rules that cost debugging time when learned the hard way:
   a plain `- id:` top-level entry is silently dropped; `insert` under an
   existing non-group id is rejected as "not a group"; first-party plugin
   packages need no profile `package.json` entry.

4. **Validate by composing, then verify live.**

   ```bash
   cd ~/.dsh && dsh --profile web --dump-config > /tmp/dump.yml
   grep ecc-hooks /tmp/dump.yml
   ```

   Compose exit status stays 0 even when the loader drops or rejects an
   entry — those problems are only reported on stderr. Confirm the entry id
   appears in the dump and stderr is empty. A live GateGuard denial on the
   session's first edit/write/bash is the visible signal the bridge is
   active.

## Updating

`git pull` reflects into linked skills immediately; regenerate the hooks
config with the same generator command. If the ECC checkout moves, regenerate
(the path is embedded in every hook command) and relink skills.

## Limits

| Surface | Status on DSH |
|---------|---------------|
| Skills | Native discovery; workflows may require host adaptation |
| Hooks | 23 command hooks on 5 of 7 bridge events |
| Slash commands | Not available (Claude Code mechanism); workflows covered by skills |
| Agents | Native dispatch unverified; use canonical prompt guidance only after review |

The validated setup here targets the CLI/web profile. Desktop profiles have a separate
installation-owned runtime and skill discovery must be verified there independently.
Generate hooks only from a reviewed ECC checkout; the linked checkout supplies their runtime.
