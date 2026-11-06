---
name: nasiko-control-plane
description: Manage the experimental Nasiko CLI lifecycle through ECC — read-only
  status checks, consent-gated install of the pinned qualified version with dry-run
  preview, and ownership-checked uninstall, under explicit telemetry and secrets boundaries.
  Use when the user asks to install, inspect, or remove the Nasiko CLI or check whether
  it is present.
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

# Nasiko CLI Lifecycle Bridge

Use this skill when a user explicitly asks ECC to install, inspect, or remove
the qualified Nasiko CLI. This skill does not operate a Nasiko control plane.

## Safety contract

- Begin with `ecc nasiko status --json`. Status is read-only.
- Installation always requires explicit user consent and `--yes`.
- Install only an ECC-qualified pinned version, currently `v0.1.0`.
- Preview first with `ecc nasiko install --version v0.1.0 --dry-run --json`.
- Install with `ecc nasiko install --version v0.1.0 --yes --json` only after the
  user reviews the version, registry origin, digest, and destination.
- Remove only a still-qualified ECC-managed binary with
  `ecc nasiko uninstall --version v0.1.0 --yes --json`. Preview removal with
  `--dry-run` first.
- The qualified source is `https://github.com/Nasiko-Labs/nasiko`, licensed
  under Apache-2.0; artifact and extracted-binary SHA-256 values are pinned.
- Never replace the qualified command with a downloaded shell or PowerShell
  bootstrap script.
- Never put secrets or credentials in command arguments, logs, skill output,
  install metadata, or ECC state.
- Nasiko telemetry and any sharing with Nasiko or Ito must be opt-in and
  separately disclosed. Installation is not telemetry consent.

## Lifecycle boundary

The initial ECC bridge supports qualified installation, read-only status, and
ownership-checked uninstall. Use the canonical Nasiko CLI directly for connection, authentication,
launch, deployment, or shutdown until those verbs have their own verified ECC
contracts. Do not guess CLI verbs.

Installing the CLI does not prove that a control-plane server is running, an
agent is governed, routing or ACLs work, observability is complete, telemetry
was enabled, or Ito compute is connected. Report each state separately.

## Failure behavior

- If the platform, architecture, version, manifest, digest, archive, binary, or
  destination fails validation, stop without executing the artifact.
- Do not fall back to `latest`.
- Do not search arbitrary `PATH` entries. Use ECC's qualified location or an
  explicit absolute `ECC_NASIKO_CLI_EXECUTABLE` for development verification.
- Do not treat a partial or ambiguous installation as success.
