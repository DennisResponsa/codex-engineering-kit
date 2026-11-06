---
name: source-command-cpp-review
description: Comprehensive C++ code review for memory safety, modern C++ idioms, concurrency,
  and security. Invokes the cpp-reviewer agent.
metadata:
  origin: ECC command
  upstream_revision: b38be6a7f6350964d59328b52f0624e1d1d552d1
  adapter: codex-engineering-kit-0.1.0
---

## Codex execution contract

Use the current Codex session model and its native tools. Model names such as Sonnet, Opus or Haiku in source examples are not model-selection instructions. Follow the current user request and project instructions before upstream workflow defaults.

Read/Grep/Glob map to native file reading and search; Bash maps to the available shell tool. Task/Agent means authorized Codex delegation, not Claude CLI. Tool frontmatter is descriptive, not a permission grant. Do not assume slash commands or Claude lifecycle hooks exist. Use a project-supported test runner and report actual results.

Resolve bundled upstream scripts and references under the plugin's `vendor/ecc/` directory. Do not use personal `~/.claude` paths or unset `CLAUDE_*` variables in Codex. Inspect example commands and translate their intent before running them. Prefer existing connected tools. Missing external services must be reported, not simulated.

Skills that specifically integrate Anthropic or another provider still require that provider; do not call those services or switch models unless requested. Do not run upstream installers, auto-updaters, learning loops, background jobs, commits, deployments or messages solely because an example suggests them. Use this distribution's documented installer for its roles.

# C++ Code Review

This command invokes the **cpp-reviewer** agent for comprehensive C++-specific code review.

## What This Command Does

1. **Identify C++ Changes**: Find modified `.cpp`, `.hpp`, `.cc`, `.h` files via `git diff`
2. **Run Static Analysis**: Execute `clang-tidy` and `cppcheck`
3. **Memory Safety Scan**: Check for raw new/delete, buffer overflows, use-after-free
4. **Concurrency Review**: Analyze thread safety, mutex usage, data races
5. **Modern C++ Check**: Verify code follows C++17/20 conventions and best practices
6. **Generate Report**: Categorize issues by severity

## When to Use

Use `/cpp-review` when:
- After writing or modifying C++ code
- Before committing C++ changes
- Reviewing pull requests with C++ code
- Onboarding to a new C++ codebase
- Checking for memory safety issues

## Review Categories

### CRITICAL (Must Fix)
- Raw `new`/`delete` without RAII
- Buffer overflows and use-after-free
- Data races without synchronization
- Command injection via `system()`
- Uninitialized variable reads
- Null pointer dereferences

### HIGH (Should Fix)
- Rule of Five violations
- Missing `std::lock_guard` / `std::scoped_lock`
- Detached threads without proper lifetime management
- C-style casts instead of `static_cast`/`dynamic_cast`
- Missing `const` correctness

### MEDIUM (Consider)
- Unnecessary copies (pass by value instead of `const&`)
- Missing `reserve()` on known-size containers
- `using namespace std;` in headers
- Missing `[[nodiscard]]` on important return values
- Overly complex template metaprogramming

## Automated Checks Run

```bash
# Static analysis
clang-tidy --checks='*,-llvmlibc-*' src/*.cpp -- -std=c++17

# Additional analysis
cppcheck --enable=all --suppress=missingIncludeSystem src/

# Build with warnings
cmake --build build -- -Wall -Wextra -Wpedantic
```

## Example Usage

```text
User: /cpp-review

Agent:
# C++ Code Review Report

## Files Reviewed
- src/handler/user.cpp (modified)
- src/service/auth.cpp (modified)

## Static Analysis Results
✓ clang-tidy: 2 warnings
✓ cppcheck: No issues

## Issues Found

[CRITICAL] Memory Leak
File: src/service/auth.cpp:45
Issue: Raw `new` without matching `delete`
```cpp
auto* session = new Session(userId);  // Memory leak!
cache[userId] = session;
```
Fix: Use `std::unique_ptr`
```cpp
auto session = std::make_unique<Session>(userId);
cache[userId] = std::move(session);
```

[HIGH] Missing const Reference
File: src/handler/user.cpp:28
Issue: Large object passed by value
```cpp
void processUser(User user) {  // Unnecessary copy
```
Fix: Pass by const reference
```cpp
void processUser(const User& user) {
```

## Summary
- CRITICAL: 1
- HIGH: 1
- MEDIUM: 0

Recommendation: FAIL: Block merge until CRITICAL issue is fixed
```

## Approval Criteria

| Status | Condition |
|--------|-----------|
| PASS: Approve | No CRITICAL or HIGH issues |
| WARNING: Warning | Only MEDIUM issues (merge with caution) |
| FAIL: Block | CRITICAL or HIGH issues found |

## Integration with Other Commands

- Use `/cpp-test` first to ensure tests pass
- Use `/cpp-build` if build errors occur
- Use `/cpp-review` before committing
- Use `/code-review` for non-C++ specific concerns

## Related

- Agent: `agents/cpp-reviewer.md`
- Skills: `skills/cpp-coding-standards/`, `skills/cpp-testing/`
