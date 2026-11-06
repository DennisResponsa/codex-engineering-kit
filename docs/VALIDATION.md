# Initial validation — 6 November 2026

- Native discovery, isolated Codex home: 350/350 skill entries enabled, zero loader errors. No model inference involved.
- All 71 role configurations parsed; all inherit the selected model and permissions.
- Eight automated distribution tests passed, covering the full catalog and source hashes, role constraints, native manifest, installer idempotence, preview, collision preservation and symlink protection.
- Deterministic rebuild produces no tracked differences.
- GitHub Actions initial run passed on Linux and macOS: https://github.com/DennisResponsa/codex-engineering-kit/actions/runs/42277580374
- Current checks: https://github.com/DennisResponsa/codex-engineering-kit/actions

This evidence does not cover behavioral execution of all specialists, external APIs or a comparison against Claude. See EVALUATION.md before making performance claims.
