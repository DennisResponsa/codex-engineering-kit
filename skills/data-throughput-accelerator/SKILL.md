---
name: data-throughput-accelerator
description: Diagnose and accelerate large data movement — ingestion, backfill, export,
  ETL, warehouse loading, manifest catch-up, and table synchronization — by isolating
  the true bottleneck, benchmarking variants, and codifying the fastest path with
  a hard accounting block proving rows and timestamps cohere. Use when a pipeline
  or backfill is too slow and must get faster without losing data correctness.
metadata:
  origin: ECC
  upstream_revision: b38be6a7f6350964d59328b52f0624e1d1d552d1
  adapter: codex-engineering-kit-0.1.0
license: MIT
---

## Codex execution contract

Use the current Codex session model and its native tools. Model names such as Sonnet, Opus or Haiku in source examples are not model-selection instructions. Follow the current user request and project instructions before upstream workflow defaults.

Read/Grep/Glob map to native file reading and search; Bash maps to the available shell tool. Task/Agent means authorized Codex delegation, not Claude CLI. Tool frontmatter is descriptive, not a permission grant. Do not assume slash commands or Claude lifecycle hooks exist. Use a project-supported test runner and report actual results.

Resolve bundled upstream scripts and references under the plugin's `vendor/ecc/` directory. Do not use personal `~/.claude` paths or unset `CLAUDE_*` variables in Codex. Inspect example commands and translate their intent before running them. Prefer existing connected tools. Missing external services must be reported, not simulated.

Skills that specifically integrate Anthropic or another provider still require that provider; do not call those services or switch models unless requested. Do not run upstream installers, auto-updaters, learning loops, background jobs, commits, deployments or messages solely because an example suggests them. Use this distribution's documented installer for its roles.

# Data Throughput Accelerator

Use this skill when the bottleneck is moving, transforming, or saving lots of
data. The goal is not just speed. The goal is faster correct data landing in the
right place with proof.

## First Distinction

Separate these before optimizing:

- source extraction speed;
- network transfer speed;
- warehouse/load speed;
- transform speed;
- serving-table freshness;
- live tail growth while the job runs.

A pipeline can be "fast" and still appear behind if new data arrives faster
than the final catch-up window.

## Fast Path Heuristics

- Move compute to where the data already is.
- Prefer warehouse-native scans, joins, and appends for large landed files.
- Use manifests or checkpoints so completed files/partitions are skipped.
- Use partitioning and clustering that match the read and append pattern.
- Batch small files, requests, and writes.
- Make writes idempotent through unique keys, manifests, or replaceable staging.
- Keep raw, derived, and serving tables separately accountable.

## Workflow

1. Read the current source, target, and manifest contracts.
2. Measure backlog: external files, manifest rows, raw rows, derived rows,
   min/max timestamps, and unprocessed counts.
3. Run a safe catch-up or sample benchmark.
4. Compare variants: batch size, worker count, warehouse SQL, file grouping,
   staging shape, and manifest update method.
5. Promote only the fastest path that keeps counts and timestamps coherent.
6. Codify the path as a CLI, scheduled job, workflow, or runbook.
7. Rerun final accounting after the codified path executes.

## Accounting Output

Use a hard accounting block:

```text
Data throughput result:
- Source files discovered: 294
- Files processed this run: 294
- Raw rows added: 9,683,598
- Derived rows added: 8,917,585
- Remaining tail: 24 files at readback time
- Runtime: 38.7s
- Correctness gate: manifest counts and table max timestamps match
```

## Guardrails

- Do not delete raw data to make a metric look better.
- Do not skip failed files silently.
- Do not mix historical backfill status with live-tail freshness.
- Do not call a pipeline complete until the target tables and manifest agree.
- For finance, healthcare, regulated, or customer-impacting data, preserve
  replay evidence and approval gates.
