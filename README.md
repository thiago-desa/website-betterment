# website betterment

Business website upgrade Grok Bot: builds or rebuilds static sites from a brief, fixes mobile and desktop layout bugs, reviews design against modern practice, and proposes a separate v2 copy without touching the live site until the owner says go.

## Problem it solves

Small business sites often look fine on a laptop and break on phones, bury the offer, and skip basic SEO and accessibility. This bot turns a brief (or a live URL) into a tested static HTML/CSS/JS site, reports gaps in plain language, and keeps redesigns in a parallel folder so nothing goes live without approval.

## How to use with Grok Bot

1. Create a new Grok Bot (suggested name: `website betterment`).
2. Paste the contents of `agents/website-betterment.md` (the **Description / system instructions** section) into the bot description / instructions.
3. Keep the skills in `skills/` alongside the bot.
4. Give it a live URL or a design brief, plus real business facts (never invent clients, numbers, or bios).
5. Review screenshots and the zip before any deploy. The bot does not publish unless you ask.

## Import into Grok Bot

Copy this bot into your own Grok Bot: [website betterment template](https://x.ai/bot/6CBsINJvglOhUtvd9LkAG)

## Key files

| Path | What it is |
|------|------------|
| `agents/website-betterment.md` | Full sanitized agent definition |
| `skills/website-upgrade.md` | Build, fix, review, and v2 playbook |
| `skills/website-getting-started.md` | First-conversation setup |
| `docs/architecture.md` | Static-site delivery model |
| `docs/workflow.md` | Brief through handoff |
| `docs/design-checklist.md` | Modern business site checklist used in reviews |
| `examples/fictional-v2-redesign.md` | Fully fictional before/after review |
| `ATTRIBUTION.md` | Design influences |
| `LICENSE` | MIT |
| `AGENTS.md` | Short agent instructions, boundaries, definition of done |
| `CONTRIBUTING.md` | How to propose changes safely |
| `docs/failure-modes.md` | Failure modes and troubleshooting |
| `evals/` | Golden-set behavioral regressions |
| `scripts/check.py` | Secrets/PII/em-dash/link hygiene checks |
| `scripts/github-workflow-checks.yml` | GitHub Actions workflow (copy to `.github/workflows/checks.yml` when the token has `workflow` scope) |

## Proof-of-work notes

This repository is a cleaned public snapshot of a working website-upgrade bot:

- Static HTML/CSS/JS deliverables with no build step required
- Mobile and desktop viewport testing (phone and laptop widths)
- Parallel v2 copies so the current site stays intact
- Explicit "nothing goes live without owner go-ahead" rule
- Fictional example only (no real firm names, emails, or team bios)

## Review findings

Portfolio review notes (repos and templates): [docs/review-2026-11-09.md in repo-operational-head](https://github.com/thiago-desa/repo-operational-head/blob/main/docs/review-2026-11-09.md).

## License and attribution

MIT License. Copyright (c) 2026 Thiago De Sa.

Design influences are listed in `ATTRIBUTION.md`.
