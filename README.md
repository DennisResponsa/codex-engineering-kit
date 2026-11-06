# Codex Engineering Kit

**A Codex-native distribution of ECC's engineering workflows: 350 skills and migrated commands, plus 71 specialist agent roles.**

Built from [ECC / Everything Claude Code](https://github.com/affaan-m/ECC), with attribution and MIT licensing preserved. Independent project; not an official OpenAI, Anthropic or ECC product.

## What changes for Codex

- A native Codex plugin exposes the complete skill catalog with normalized frontmatter and an explicit Codex execution contract.
- 71 native TOML role templates inherit your selected model and permissions. No Claude subscription or Anthropic model is required to use the general engineering workflows.
- A project-scoped installer adds roles without replacing your model, provider, existing agents or permission settings. It supports preview, collision detection and repeatable installation.
- Source checksums and a pinned upstream revision make the adaptation reproducible.
- No automatic hooks, MCP servers, learning loops or background agents are enabled by this distribution.

This is a workflow and instruction toolkit, **not a model, security boundary or performance guarantee**. Provider-specific skills still require their respective products. Installing the catalog does not verify every integration. See [compatibility and validation](docs/COMPATIBILITY.md).

## Install the skill plugin

Requires a Codex release with native repository marketplace support. Tested locally with Codex CLI `0.167.0-alpha.3.2`; compatibility with other versions should be checked.

```sh
codex plugin marketplace add DennisResponsa/codex-engineering-kit
codex plugin add codex-engineering-kit@codex-engineering-kit
codex plugin list --json
```

Start a new Codex session to discover the skills. Use ordinary requests such as “Review this change for correctness and security, then run the relevant tests.” Select relevant skills; loading the entire catalog into one task is unnecessary.

If you already use ECC, avoid enabling both complete catalogs in the same session unless you intentionally want duplicate workflows. This installer never silently removes another plugin.

## Install the 71 agent roles

Python 3.11+ is required. Installing roles does not start agents or enable parallel execution.

```sh
git clone https://github.com/DennisResponsa/codex-engineering-kit.git
cd codex-engineering-kit
python3 scripts/install_agents.py --project /path/to/your/project --dry-run
python3 scripts/install_agents.py --project /path/to/your/project
```

Roles are named `cek_code_reviewer`, `cek_architect`, and so on. They are written under the target project's `.codex/agents/cek/` and registered in `.codex/config.toml`. Existing settings are preserved; the first pre-install config is backed up locally as `config.toml.before-cek`. Keep that backup private. The user and host decide when delegation is permitted and how many agents may run.

## Validate and rebuild

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/check_release.py
```

If Codex CLI is installed, perform an actual isolated discovery test without using your normal Codex configuration:

```sh
python scripts/check_native.py
```

The discovery test creates a temporary Codex home, registers only this plugin and checks `skills/list`. It does not call an AI model, authenticate another account or modify your usual Codex setup.

## Evidence and limits

The release tests cover all catalog entries and role configs, source integrity, installer idempotence, collision handling and symlink refusal. Native discovery is tested separately. These checks do **not** demonstrate that all 71 agents perform their specialties correctly or that all external services work.

There is no claim of superiority over Claude. A meaningful comparison needs the same tasks, starting code, tools, budgets and independently checked outcomes. See [the evaluation protocol](docs/EVALUATION.md).

## Source and license

The untouched upstream snapshot is in `vendor/ecc/`, pinned to `b38be6a7f6350964d59328b52f0624e1d1d552d1`. It includes upstream resources and scripts for reference; its own installers and workflows are not automatically activated. Generate adapters with `scripts/build.py` rather than editing generated files.

[Full catalog](docs/CATALOG.md) · [Attribution](NOTICE.md) · [MIT license](LICENSE)
