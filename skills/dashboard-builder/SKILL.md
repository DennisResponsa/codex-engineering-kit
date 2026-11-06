---
name: dashboard-builder
description: Build monitoring dashboards that answer real operator questions for Grafana,
  SigNoz, and similar platforms. Use when turning metrics into a working dashboard
  instead of a vanity board.
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

# Dashboard Builder

Use this when the task is to build a dashboard people can operate from.

The goal is not "show every metric." The goal is to answer:

- is it healthy?
- where is the bottleneck?
- what changed?
- what action should someone take?

## When to Use

- "Build a Kafka monitoring dashboard"
- "Create a Grafana dashboard for Elasticsearch"
- "Make a SigNoz dashboard for this service"
- "Turn this metrics list into a real operational dashboard"

## Guardrails

- do not start from visual layout; start from operator questions
- do not include every available metric just because it exists
- do not mix health, throughput, and resource panels without structure
- do not ship panels without titles, units, and sane thresholds

## Workflow

### 1. Define the operating questions

Organize around:

- health / availability
- latency / performance
- throughput / volume
- saturation / resources
- service-specific risk

### 2. Study the target platform schema

Inspect existing dashboards first:

- JSON structure
- query language
- variables
- threshold styling
- section layout

### 3. Build the minimum useful board

Recommended structure:

1. overview
2. performance
3. resources
4. service-specific section

### 4. Cut vanity panels

Every panel should answer a real question. If it does not, remove it.

## Example Panel Sets

### Elasticsearch

- cluster health
- shard allocation
- search latency
- indexing rate
- JVM heap / GC

### Kafka

- broker count
- under-replicated partitions
- messages in / out
- consumer lag
- disk and network pressure

### API gateway / ingress

- request rate
- p50 / p95 / p99 latency
- error rate
- upstream health
- active connections

## Quality Checklist

- [ ] valid dashboard JSON
- [ ] clear section grouping
- [ ] titles and units are present
- [ ] thresholds/status colors are meaningful
- [ ] variables exist for common filters
- [ ] default time range and refresh are sensible
- [ ] no vanity panels with no operator value

## Related Skills

- `research-ops`
- `backend-patterns`
- `terminal-ops`
