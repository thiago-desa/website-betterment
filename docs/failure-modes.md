# Failure modes and troubleshooting

## Content failures

| Failure | What it looks like | What to do |
|---------|--------------------|------------|
| Invented testimonial | Fake client quote | Delete; ask owner for real copy |
| Wrong phone/email on site | Stale config | Single config source; re-read brief |
| Em dash in copy | U+2014 in paragraphs | Rewrite per owner rule |

## Delivery failures

| Failure | What it looks like | What to do |
|---------|--------------------|------------|
| Live overwrite | Edited production in place for a redesign | Move work to `site-v2`; restore prior copy if needed |
| Mobile break | Horizontal scroll at 390px | Fix CSS; re-screenshot |
| Unasked deploy | Published without owner go-ahead | Treat as incident; pull back if possible |

## Verification (design)

Viewport screenshots and a short design-checklist pass are the sensors. Parallel folders are the recovery path. Human approval is the release gate.
