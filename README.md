# Codex Engineering Kit

[![Validate distribution](https://github.com/DennisResponsa/codex-engineering-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/DennisResponsa/codex-engineering-kit/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Give Codex a repeatable workflow for planning, building, testing and reviewing software.**

Codex Engineering Kit adapts [ECC / Everything Claude Code](https://github.com/affaan-m/ECC) into a native Codex skill plugin and project-scoped specialist roles. Use the model you already selected in Codex. Start with one task, load the relevant guidance, and verify the result.

**350 skills and migrated commands · 71 specialist role templates · No automatic background agents**

[Try the demo](#try-it-first-no-account-required) · [Install](#install-in-codex) · [Full catalog](docs/CATALOG.md) · [Latest release](https://github.com/DennisResponsa/codex-engineering-kit/releases/latest)

## What can I do with it?

| Your task | Example workflow |
| --- | --- |
| Start an application | Clarify acceptance criteria → plan architecture → implement → test → review |
| Fix a bug | Reproduce it → add a failing test → make a focused change → verify independently |
| Review an existing project | Inspect a bounded area → run relevant checks → report reproduced issues and limits |
| Prepare a release | Check compatibility, tests, attribution and publication boundaries |

These are workflows you can request, not promises that every project completes unattended. Agent delegation depends on your Codex host and permissions. External services require their own configuration. A general engineering workflow does not require a Claude subscription; product-specific skills may still depend on the product they describe.

## Try it first: no account required

The included demo uses **only synthetic data**, Python 3.11+ and its standard library. No credentials, network access or AI model calls.

```sh
git clone https://github.com/DennisResponsa/codex-engineering-kit.git
cd codex-engineering-kit
python3 examples/order_totals/run_demo.py
```

The example catches a discount incorrectly applied to shipping:

| Same eight acceptance tests | Outcome |
| --- | --- |
| Intentionally faulty fixture | 2 fail: shipping was discounted |
| Corrected implementation | 8 pass |

The demo command exits successfully only when both expected outcomes match. **It runs tests, not agents.** To try a real delegated Codex review, use the prompt in the [demo guide](examples/order_totals/README.md). The solution is included for inspection; this is not a model benchmark.

## Install in Codex

### 1. Enable the skill plugin

Requires a Codex release with native repository marketplace support. Native discovery was tested with CLI `0.167.0-alpha.3.2`; other versions must be checked rather than assumed compatible.

```sh
codex plugin marketplace add DennisResponsa/codex-engineering-kit
codex plugin add codex-engineering-kit@codex-engineering-kit
codex plugin list --json
```

Start a new Codex session. If you already have the full ECC plugin enabled, choose one catalog for that session to avoid duplicate workflows. Nothing here silently removes another plugin.

### 2. Add specialist roles to your project (optional)

From the cloned repository, with Python 3.11+:

```sh
python3 scripts/install_agents.py --project /path/to/your/project --dry-run
python3 scripts/install_agents.py --project /path/to/your/project
```

Replace `/path/to/your/project` with your actual project directory. Roles such as `cek_code_reviewer` and `cek_architect` are registered in that project's `.codex/config.toml`; templates live in `.codex/agents/cek/`. They inherit your model and permissions. The installer checks collisions and preserves existing settings. Its private local backup, `config.toml.before-cek`, should not be committed.

Installing roles does not launch agents or grant permissions. Restart the project session to load the configuration.

### 3. Give Codex a bounded task

> Use Codex Engineering Kit to review this project. Start with its project instructions. Use a test analyst and an independent reviewer if delegation is available. Reproduce issues locally, report the tests run and their limits, and do not publish or contact external services.

Select skills relevant to the task; do not load all 350 at once. For a first run with known data, use [the order totals demo](examples/order_totals/README.md).

### If setup does not work

- **Unknown `plugin` command:** your Codex build may not support the tested marketplace interface. Check its own help/version; do not run upstream Claude installers as a substitute.
- **Skills not visible:** check `codex plugin list --json` and start a new session. Use the isolated discovery check below to separate catalog errors from normal-profile configuration.
- **Roles not visible:** confirm the target project and its `.codex/config.toml`; start a session for that project. The host must support custom roles.
- **Installer collision:** inspect the named existing entry. The installer intentionally stops instead of replacing unrelated configuration.

[Compatibility, dependencies and uninstall](docs/COMPATIBILITY.md)

## What is verified?

- Distribution tests cover every generated catalog entry, upstream source hashes, all 71 TOML role files, model inheritance and installer behavior.
- Native plugin discovery is tested separately using a temporary Codex home.
- The demo checks eight acceptance cases against a faulty fixture and a corrected example.
- CI runs distribution checks and the demo on Linux and macOS. See the badge and [validation record](docs/VALIDATION.md) for actual outcomes.

These checks do **not** certify the behavior of every specialist, every external integration or production security. The kit is instruction-based guidance, not a model, security boundary or always-running autonomous service. No hooks, MCP servers, learning loops or background agents are automatically enabled.

## Develop and validate

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/build.py
python -m unittest discover -s tests -v
python examples/order_totals/run_demo.py
python scripts/check_release.py
```

With a compatible Codex CLI available:

```sh
python scripts/check_native.py
```

This uses a temporary `CODEX_HOME`, tests plugin discovery, and does not invoke a model or alter your normal configuration. Regenerate adapters with `scripts/build.py`; do not hand-edit generated skill or role files.

## Help improve the kit

Try the demo, then one bounded task in your own project. [Report a reproducible issue](https://github.com/DennisResponsa/codex-engineering-kit/issues) with your Codex version, OS, command and expected/observed result. Remove credentials, private paths and customer data before posting. Improvements to onboarding, compatibility evidence and synthetic examples are welcome; read [CONTRIBUTING.md](CONTRIBUTING.md).

If the kit is useful, a star helps other people discover it. More valuable still: tell us what worked, what failed, and how to reproduce it.

## Attribution and license

Independent project maintained by **DennisResponsa**, derived from **ECC / Everything Claude Code**. Not an official OpenAI, Anthropic or ECC product. The upstream MIT license and attribution are preserved.

The unchanged upstream snapshot under `vendor/ecc/` is pinned to `b38be6a7f6350964d59328b52f0624e1d1d552d1`. Bundled upstream scripts are reference material, not automatically executed installers. This release updates onboarding and the demo; the generated adapter contract remains version 0.1.0.

No superiority over Claude is claimed. A meaningful comparison needs matched tasks, tools, budgets and independently checked outcomes: see [EVALUATION.md](docs/EVALUATION.md).

[MIT license](LICENSE) · [Attribution](NOTICE.md) · [Compatibility](docs/COMPATIBILITY.md)
