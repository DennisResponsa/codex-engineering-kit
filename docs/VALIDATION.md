# Initial validation — 6 November 2026

- Native discovery, isolated Codex home: 350/350 skill entries enabled, zero loader errors. No model inference involved.
- All 71 role configurations parsed; all inherit the selected model and permissions.
- Eight automated distribution tests passed, covering the full catalog and source hashes, role constraints, native manifest, installer idempotence, preview, collision preservation and symlink protection.
- Deterministic rebuild produces no tracked differences.
- GitHub Actions initial run passed on Linux and macOS: https://github.com/DennisResponsa/codex-engineering-kit/actions/runs/42277580374
- Current checks: https://github.com/DennisResponsa/codex-engineering-kit/actions

This evidence does not cover behavioral execution of all specialists, external APIs or a comparison against Claude. See EVALUATION.md before making performance claims.

## v0.1.1 - 9 November 2026

- Rebuilt adapters: 350 skills and 71 role templates; no generated changes.
- Distribution tests: 8/8 passed.
- Native discovery repeated with Codex CLI 0.167.0-alpha.3.2 in a temporary CODEX_HOME: 350 loaded/enabled, zero errors.
- Synthetic demo: same 8 tests, exactly 2 expected failures against the faulty fixture and 8/8 passed against the corrected example. No model invoked.
- Independent Python and release reviews approved the changed example and onboarding documentation.
- Linux/macOS CI now includes the demo. Consult the workflow for the tagged release commit for its remote result.

The intentionally faulty implementation is a teaching fixture, not evidence that agents discovered a previously unknown bug. No client code or operational data was used.
