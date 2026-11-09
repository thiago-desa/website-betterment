# AGENTS.md

Short, high-signal instructions for coding agents working in `website-betterment`.

## What this repo is

Business website upgrade Grok Bot: static builds from a brief, mobile/desktop testing, design review, and parallel v2 copies that never go live unasked.

This is a sanitized proof-of-work snapshot of a Grok Bot design. Markdown skills and docs are the product. There is no service binary to compile.

## Layout

| Path | Role |
|------|------|
| `agents/` | Sanitized agent definition |
| `skills/` | Upgrade playbook and getting started |
| `docs/` | Architecture, workflow, design checklist, failure modes |
| `evals/` | Golden set of fictional site tasks |
| `examples/` | Fictional v2 redesign |
| `scripts/check.py` | Hygiene CI entrypoint |

## Commands

```bash
python scripts/check.py
```

## Hard boundaries

- Never invent clients, metrics, testimonials, credentials, or bios.
- Never deploy live unless the owner explicitly asked.
- Keep firm facts in one config file; static HTML/CSS/JS by default.
- Larger redesigns land in a parallel `site-v2` (or similar) folder.
- No em dashes or en dashes when the owner forbids them (portfolio default: forbid).
- No secrets in the repo.

## Definition of done

- Pages tested at roughly 390x844 and 1366x900 mentally or via screenshots.
- No sideways scroll / script errors in the stated deliverable.
- `python scripts/check.py` passes.
- README import link intact; Key files updated.

## Ownership

Maintained by Thiago De Sa. Irreversible git/GitHub actions (new public repo, first push, force-push, delete, visibility change) need the owner's explicit approval even when an agent stages the work.
