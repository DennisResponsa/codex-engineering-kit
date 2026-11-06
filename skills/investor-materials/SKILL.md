---
name: investor-materials
description: Create and update pitch decks, one-pagers, investor memos, accelerator
  applications, financial models, and fundraising materials. Use when the user needs
  investor-facing documents, projections, use-of-funds tables, milestone plans, or
  materials that must stay internally consistent across multiple fundraising assets.
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

# Investor Materials

Build investor-facing materials that are consistent, credible, and easy to defend.

## When to Activate

- creating or revising a pitch deck
- writing an investor memo or one-pager
- building a financial model, milestone plan, or use-of-funds table
- answering accelerator or incubator application questions
- aligning multiple fundraising docs around one source of truth

## Golden Rule

All investor materials must agree with each other.

Create or confirm a single source of truth before writing:
- traction metrics
- pricing and revenue assumptions
- raise size and instrument
- use of funds
- team bios and titles
- milestones and timelines

If conflicting numbers appear, stop and resolve them before drafting.

## Core Workflow

1. inventory the canonical facts
2. identify missing assumptions
3. choose the asset type
4. draft the asset with explicit logic
5. cross-check every number against the source of truth

## Asset Guidance

### Pitch Deck
Recommended flow:
1. company + wedge
2. problem
3. solution
4. product / demo
5. market
6. business model
7. traction
8. team
9. competition / differentiation
10. ask
11. use of funds / milestones
12. appendix

If the user wants a web-native deck, pair this skill with `frontend-slides`.

### One-Pager / Memo
- state what the company does in one clean sentence
- show why now
- include traction and proof points early
- make the ask precise
- keep claims easy to verify

### Financial Model
Include:
- explicit assumptions
- bear / base / bull cases when useful
- clean layer-by-layer revenue logic
- milestone-linked spending
- sensitivity analysis where the decision hinges on assumptions

### Accelerator Applications
- answer the exact question asked
- prioritize traction, insight, and team advantage
- avoid puffery
- keep internal metrics consistent with the deck and model

## Red Flags to Avoid

- unverifiable claims
- fuzzy market sizing without assumptions
- inconsistent team roles or titles
- revenue math that does not sum cleanly
- inflated certainty where assumptions are fragile

## Quality Gate

Before delivering:
- every number matches the current source of truth
- use of funds and revenue layers sum correctly
- assumptions are visible, not buried
- the story is clear without hype language
- the final asset is defensible in a partner meeting
