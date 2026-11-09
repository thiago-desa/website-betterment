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

<!-- TEMPLATE_SHARE_LINK: paste the public Grok Bot template URL here once the bot has exported and the owner has confirmed the review card. -->
_Template link pending owner confirmation._

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

## Proof-of-work notes

This repository is a cleaned public snapshot of a working website-upgrade bot:

- Static HTML/CSS/JS deliverables with no build step required
- Mobile and desktop viewport testing (phone and laptop widths)
- Parallel v2 copies so the current site stays intact
- Explicit "nothing goes live without owner go-ahead" rule
- Fictional example only (no real firm names, emails, or team bios)

## License and attribution

MIT License. Copyright (c) 2026 Thiago De Sa.

Design influences are listed in `ATTRIBUTION.md`.
