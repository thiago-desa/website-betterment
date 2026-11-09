# Architecture

website betterment delivers static sites from a working folder on the bot's computer, not by editing production blindly.

## Delivery model

- Working copy in a folder (for example `site/`)
- Larger redesigns in a sibling folder (for example `site-v2/`)
- Zip archives for handoff to the owner or a deploy bot
- Screenshots at phone and laptop widths as acceptance evidence

## Separation of concerns

| Role | Responsibility |
|------|----------------|
| website betterment | Design, build, fix, review, zip |
| Owner | Approve copy, facts, and go-live |
| Optional deploy bot | Publish only after owner approval |

## What this repo is

A public-ready snapshot of the agent definition, upgrade skill, design checklist, and a fictional redesign example. It does not include any real business site files.
