# Evaluation protocol

Compare three conditions: Codex without the toolkit, Codex with the toolkit, and a separately authorized Claude baseline. Use the same repository revision, task, tool availability, time/token budget and acceptance tests. Record exact model and runtime versions.

Select public fixtures or explicitly authorized sanitized projects. Include a bug fix, a feature change and a security review with known ground truth. Hidden acceptance tests should be prepared before runs. Repeat trials to distinguish variation from a reliable advantage.

Record acceptance tests passed, regressions, false positive findings, task time, tokens/cost when measurable, and human interventions. Preserve diffs and command exit codes. Report unsuccessful and incomplete trials. Skill counts, stars and a successful toy test are not performance evidence.

Do not publish private repositories, customer data, prompts containing secrets or local session logs. No comparative results are claimed by the initial release.
