---
name: benchmark-optimization-loop
description: Convert 'make it faster' requests into a bounded measured optimization
  loop — baseline first, generate one-hypothesis variants, benchmark each against
  a correctness gate, and promote the fastest safe variant with reproducible commands.
  Use when asked to speed something up, try many variants, run recursive optimization,
  benchmark latency/throughput/cost, or pick the best implementation by repeated measured
  tests.
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

# Benchmark Optimization Loop

Use this skill to convert "make it 20x faster" or "try 50 recursive
optimizations" into a bounded measured loop that can actually improve a system.

## Required Baseline

Do not optimize until these exist:

- the operation being optimized;
- the correctness gate that must stay green;
- the metric: wall time, p95 latency, rows/sec, cost/run, memory, error rate;
- the current baseline;
- the search budget: max variants, max time, max spend, max data impact.

If the user asks for an unrealistic target, keep the ambition but make the loop
bounded and measurable.

## Loop

1. Measure the baseline.
2. Identify bottlenecks from evidence.
3. Generate variants that test one hypothesis each.
4. Run variants with the same input shape.
5. Reject variants that fail correctness, safety, or reproducibility.
6. Promote the fastest safe variant.
7. Codify the winning path in a script, command, test, config, or doc.
8. Rerun the baseline and winner to confirm the delta.

## Variant Table

Track variants like this:

```text
Variant | Hypothesis | Command | Time | Correct? | Notes
baseline | current path | npm run job | 120s | yes | stable
batch-500 | fewer round trips | npm run job -- --batch 500 | 42s | yes | winner
parallel-8 | more workers | npm run job -- --workers 8 | 31s | no | rate limited
```

## Recursive Search

For recursive or hyperparameter work:

- persist every run to a ledger;
- compare against the prior accepted winner, not only the previous run;
- keep a holdout or replay check;
- stop when improvement is within noise, correctness fails, cost exceeds the
  budget, or the search starts changing more variables than it can explain.

Use phrases like "best measured safe variant" instead of "global optimum" unless
the search space was actually exhaustive.

## Promotion Gate

A variant cannot become the new default until:

- correctness tests pass;
- the performance delta is repeated or explained;
- rollback is obvious;
- the change is encoded in source control or a durable runbook;
- the final summary includes exact commands and measurements.
