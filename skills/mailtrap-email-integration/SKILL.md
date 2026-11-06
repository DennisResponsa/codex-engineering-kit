---
name: mailtrap-email-integration
description: Guides agents through integrating transactional email sending via Mailtrap's
  Email API, including sandbox testing, domain verification, and API authentication.
  Use when implementing email-sending features, debugging delivery issues, or setting
  up safe dev/staging email testing.
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

# Mailtrap Email Integration

Patterns for adding transactional email sending to an application using Mailtrap's Email API and Sandbox, covering authentication, environment separation, and common delivery pitfalls.

## When to Activate

- Implementing a "send email" feature (signup confirmation, password reset, notifications, receipts)
- Debugging why emails aren't arriving in dev/staging
- Setting up a project's first email-sending integration
- Reviewing code that calls an email API directly without sandbox separation

## Core Concepts

**Sandbox vs. Production separation.** Mailtrap provides a Sandbox API that captures emails without delivering them, used for dev/staging so test emails never reach real inboxes. Production sending uses a separate, verified-domain endpoint. Never point a dev environment at the production sending endpoint.

**Authentication.** Requests use a Bearer token in the `Authorization` header. Tokens are scoped per project; sandbox and production typically use different tokens.

**Domain verification.** Production sending requires verifying a sending domain via DNS records (SPF, DKIM, DMARC) before Mailtrap will deliver to real recipients. Skipping this causes silent delivery failures or spam-folder placement.

## Code Examples

```typescript
// Sending via Mailtrap's Email API (production)
async function sendEmail(to: string, subject: string, html: string) {
  const response = await fetch("https://send.api.mailtrap.io/api/send", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.MAILTRAP_API_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: { email: "no-reply@yourverifieddomain.com", name: "Your App" },
      to: [{ email: to }],
      subject,
      html,
    }),
  });

  if (!response.ok) {
    throw new Error(`Email send failed: ${response.status}`);
  }
  return response.json();
}
```

```typescript
// Same call, routed to Sandbox in non-production environments
const MAILTRAP_ENDPOINT = process.env.NODE_ENV === "production"
  ? "https://send.api.mailtrap.io/api/send"
  : `https://sandbox.api.mailtrap.io/api/send/${process.env.MAILTRAP_INBOX_ID}`;
```

## Anti-Patterns

| Anti-Pattern | Why It's a Problem | Instead |
| --- | --- | --- |
| Using the production sending endpoint in dev/test | Real test emails reach real inboxes, risking spam complaints and leaked test data | Route non-production environments to the Sandbox endpoint |
| Hardcoding API tokens in source | Credential leak risk if committed to version control | Load tokens from environment variables / secrets manager |
| Sending before domain verification completes | Emails silently fail or land in spam | Verify SPF/DKIM/DMARC records before enabling production sending |
| No retry/error handling on send failures | Silent notification failures (e.g., user never gets password reset email) | Check response status, log failures, surface actionable errors |

## Best Practices

- Keep sandbox and production tokens in separate environment variables, never share one token across environments
- Verify sending domain DNS records before any production launch involving email
- Log delivery failures with enough context to debug (recipient, template, timestamp, response code)
- Treat email sending as a fallible network call: wrap in try/catch, never assume success

## Related Skills

`api-and-interface-design`, `security-and-hardening`, `ci-cd-and-automation`
