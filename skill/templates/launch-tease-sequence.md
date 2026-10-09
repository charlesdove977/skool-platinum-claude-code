# Launch Tease Sequence Template

## Contents
- Template block (fenced)
- Field Documentation
- Section Specifications

Output file: `skool-platinum/launch/{group-slug}/{YYYY-MM-DD}/tease-drip.md`

```template
# 5-day tease: {group-name} · launch {launch-date} · primary platform {platform}

| Day | Reveal | IG story / broadcast | YouTube community post |
|---|---|---|---|
| 1 | Something is coming | [story script + broadcast-channel CTA] | [post] |
| 2 | Who it's for | "If you're [audience], I'm building something for you..." | [post] |
| 3 | The pain + outcome | [pain you keep seeing] → [outcome it delivers] | [post] |
| 4 | Sneak peek: deliverable 1 | [deliverable 1] → [specific benefit] | [post] |
| 5 | Deliverables 2 + 3, doors open tomorrow | [deliverables 2, 3] → [outcome] | [post] |
| Launch | Doors open | [launch post + CTA] | [launch post + pinned comment] |
```

## Field Documentation
| Field | Type | Notes |
|---|---|---|
| {launch-date}, {platform} | variable | From gather_launch_facts |
| Deliverables | prose | From the approved offer/deliverables |

## Section Specifications
- **Drip, never dump**: each day reveals one more piece.
- **Every day ends with one action** (join broadcast, turn on notifications, comment a keyword).
