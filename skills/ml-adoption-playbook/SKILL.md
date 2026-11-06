---
name: ml-adoption-playbook
description: End-to-end methodology for AI agents and software engineers to add machine
  learning algorithms to existing non-ML codebases. Covers problem framing, data readiness,
  architectural decoupling, and baseline model integration. Use when adding a machine
  learning capability to a codebase that has none, from problem framing through a
  baseline model.
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

# ML Adoption Playbook

This skill provides an adaptive methodology for implementing machine learning models into existing software engineering projects. It bridges the gap between traditional SWE and MLOps by structuring how ML should be researched, decoupled, trained, and integrated.

## When to Activate

- A user asks to "add ML" or "add an algorithm" to their existing codebase.
- Planning the integration of a new model (e.g., recommendation, classification, forecasting) into a non-ML application.
- Structuring a workflow for an agent to build, train, and deploy an ML component adaptively.

## Phase 1: Problem Framing & Feasibility

Before writing model code, establish the "why" and "how".
- **Heuristic Check:** Ask the user if a simple heuristic (e.g., regex, rule-based sorting) could solve the problem faster. If yes, start there.
- **Metric Definition:** Define what business metric the ML model is trying to improve (e.g., click-through rate, reduced latency).
- **Mistake Budget:** Define what a "bad" prediction looks like and how the system should handle it.

## Phase 2: Data Readiness

ML is useless without clean, accessible data.
- **Audit Data Sources:** Identify where the training data lives. Is it a live database, a static CSV, or an API?
- **Data Contract:** Establish a schema for the input data. What features are required? What happens if a feature is missing?
- **Leakage Prevention:** Ensure the user's proposed data split does not accidentally leak future information into the training set (e.g., chronological splitting for time-series data).

## Phase 3: Architectural Integration & Decoupling

Do not tightly couple model inference to core business logic.
- **API Boundary:** Suggest placing the model behind an API endpoint (e.g., using `fastapi-patterns` or `django-patterns`) or a dedicated service class.
- **Fallback Mechanisms:** Design a default state. If the model takes too long to respond or throws an error, the system must gracefully fall back to a hardcoded rule.
- **Feature Flags:** Wrap the new ML inference call in a feature flag so it can be rolled out (or rolled back) safely.

## Phase 4: Model Implementation & Training

Structure the code for reproducibility and iteration.
- **Start Simple:** Build a baseline model first (e.g., a simple scikit-learn Logistic Regression or a barebones PyTorch linear layer).
- **Reproducibility:** Apply `pytorch-patterns` or similar best practices: fix random seeds, make code device-agnostic, and explicitly document tensor/array shapes.
- **Automated Evidence:** Require tests for the data transforms and inference schema. Do not accept a model without an evaluation script comparing it against the baseline.

## Phase 5: Handoff to MLOps

Once the baseline model is integrated, shift focus to continuous operations.
- **Refer to `mle-workflow`:** Guide the user toward setting up experiment tracking, model registries, and drift detection.
- **CI/CD:** Add the model evaluation step to the existing CI pipeline to ensure future commits do not degrade model performance.

## Iterative Agent Workflow

When assisting a user via this playbook, agents should:
1. **Ask clarifying questions** to complete Phase 1 before proposing architectures.
2. **Draft a data contract** in Phase 2 for user approval.
3. **Write the decoupling interface** (API/Service) in Phase 3 *before* writing the training loop.
4. **Deliver a reproducible script** in Phase 4 that trains the model and saves the artifact.
