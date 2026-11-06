# Compatibility and validation

## Scope

The catalog contains 314 canonical ECC skills plus 36 source commands migrated into skill entrypoints. These 36 names are pinned in scripts/migrated_commands.json; all original commands remain available as upstream reference material. There are 71 generated specialist role templates.

Skill frontmatter is normalized for Codex. Each entry receives the Codex execution contract, removes Claude-specific frontmatter routing, and keeps its original specialized guidance. Source text that describes a particular product, API or shell environment is retained rather than incorrectly renamed. The catalog flags source host references and credential indicators; those flags are hints, not exhaustive dependency classifications.

## Capability boundaries

| Surface | Support | Evidence needed |
| --- | --- | --- |
| Skill discovery | Native plugin | Actual Codex skills/list reports all 350 entries |
| Agent role syntax | Native TOML | All 71 files parse; project installer tests pass |
| Model selection | Inherited | No generated role contains a model/provider override |
| Tool use | Adapted instructions | Map read/search/shell/delegation to available native tools |
| External products and APIs | Conditional | Install/configure the particular service and test an authorized operation |
| Claude-only tooling and hooks | Not emulated | The underlying product remains a separate dependency |
| Upstream helper scripts | Bundled, not automatically executed | Inspect source and install the required runtime when a task needs it |
| Security isolation | Not provided | Must be enforced by the runtime/OS independently |

For bundled scripts, use the actual plugin directory's vendor/ecc path. Never execute a command with unresolved CLAUDE_* variables or assume a personal ~/.claude folder exists. Equivalent native connectors can replace a service only when they provide the required behavior. No skill authorizes external writes by itself.

## Checks

The test suite examines every generated entry, verifies upstream source hashes and checks actual installer behavior in temporary projects. The optional native check uses a temporary CODEX_HOME and does not invoke an AI model. GitHub Actions runs the deterministic build and tests on Linux and macOS; check the repository's run results for current status.

These are integration checks, not end-to-end behavioral certification of the entire catalog. A task-specific trial is required before relying on any specialized workflow. This release has not benchmarked itself against Claude.

## Updates

Do not use vendor/ecc's legacy global sync or auto-update scripts to update this derivative. Review a new upstream revision, replace the pinned vendor snapshot deliberately, regenerate and re-run validation. The initial builder is pinned to one revision and is not a complete automatic upstream updater.

## Uninstall

Remove the plugin with Codex's plugin manager. To remove project roles, remove only the marked CODEX ENGINEERING KIT block from .codex/config.toml and the .codex/agents/cek directory. Preserve unrelated settings. Do not blindly restore an old backup after other project settings have changed.
