---
name: latency-critical-systems
description: Optimize and verify latency-sensitive systems — realtime dashboards,
  market data feeds, streaming agents, execution gateways, queues, and caches — by
  tracking p50/p95/p99 latency, freshness age, and queue depth, mapping hot paths,
  and running live readbacks. Use when p95 latency, throughput, or data freshness
  matters.
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

# Latency Critical Systems

Use this skill when the user cares about realtime behavior, hot paths, streaming
freshness, or execution speed. This includes HFT-like infrastructure, but the
skill is engineering-focused. It does not authorize live trading or financial
advice.

## Split The Metrics

Do not collapse everything into "fast." Track:

- p50, p95, and p99 latency;
- throughput;
- freshness age;
- queue depth;
- cache hit rate;
- provider/API response time;
- browser render time;
- correctness under load;
- failure and retry behavior.

## Map The Hot Path

Write the path from user/event to final visible state:

```text
source event -> provider API -> ingest worker -> queue -> cache -> edge route
-> client stream -> browser render -> user-visible state
```

Then measure each segment separately.

## Optimization Order

1. Remove unnecessary round trips.
2. Cache stable reads with freshness metadata.
3. Batch small calls and writes.
4. Move compute closer to the data or the user.
5. Split hot and cold paths.
6. Apply backpressure before queues grow unbounded.
7. Use streaming only when it improves freshness or user experience.
8. Add canaries for stale data, degraded providers, and bad cache state.

## Verification

Use live readbacks when a deployed surface exists:

- HTTP timing and response headers;
- provider freshness timestamp;
- queue or job state;
- edge/cache state;
- browser verification for actual UI freshness;
- logs around retries and degraded mode.

For market-data or execution-adjacent paths, also verify orderbook age, VWAP
assumptions, provider status, and kill-switch behavior before calling the path
ready.

## Guardrails

- Do not optimize latency by dropping required validation.
- Do not hide stale data behind fast cache hits.
- Do not claim millisecond behavior from client labels without measurement.
- Do not run live orders, destructive migrations, or customer-impacting deploys
  without an explicit approval gate.
- Keep secrets and private payloads out of logs and benchmark artifacts.
