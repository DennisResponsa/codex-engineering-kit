---
name: google-workspace-ops
description: Operate across Google Drive, Docs, Sheets, and Slides as one workflow
  surface for plans, trackers, decks, and shared documents. Use when the user needs
  to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping
  to raw tool calls.
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

# Google Workspace Ops

This skill is for operating shared docs, spreadsheets, and decks as working systems, not just editing one file in isolation.

## When to Use

- User needs to find a doc, sheet, or deck and update it in place
- Consolidating plans, trackers, notes, or customer lists stored in Google Drive
- Cleaning or restructuring a shared spreadsheet
- Importing, repairing, or reformatting a Google Slides deck
- Producing summaries from Docs, Sheets, or Slides for decision-making

## Preferred Tool Surface

Use Google Drive as the entry point, then switch to the right specialist:

- Google Docs for text-heavy docs
- Google Sheets for tabular work, formulas, and charts
- Google Slides for decks, imports, template migration, and cleanup

Do not guess structure from filenames alone. Inspect first.

## Workflow

### 1. Find the asset

Start with the Drive search surface to locate:

- the exact file
- sibling assets
- likely duplicates
- recently modified versions

If several documents look similar, confirm by title, owner, modified time, or folder.

### 2. Inspect before editing

Before making changes:

- summarize current structure
- identify tabs, headings, or slide count
- detect whether the task is local cleanup or structural surgery

Pick the smallest tool that can safely perform the work.

### 3. Edit with precision

- For Docs: use index-aware edits, not vague rewrites
- For Sheets: operate on explicit tabs and ranges
- For Slides: distinguish content edits from visual cleanup or template migration

If the requested work is visual or layout-sensitive, iterate with inspection and verification instead of one giant blind update.

### 4. Keep the working system clean

When the file is part of a larger workflow, also surface:

- duplicate trackers
- outdated decks
- stale docs vs canonical docs
- whether the asset should be archived, merged, or renamed

## Output Format

Use:

```text
ASSET
- file name
- type
- why this is the right file

CURRENT STATE
- structure summary
- key problems or blockers

ACTION
- edits made or recommended

FOLLOW-UPS
- archive / merge / duplicate cleanup / next file to update
```

## Good Use Cases

- "Find the active planning doc and condense it"
- "Clean up this customer spreadsheet and show me the churn-risk rows"
- "Import this deck into Slides and make it presentable"
- "Find the current tracker, not the stale duplicate"
