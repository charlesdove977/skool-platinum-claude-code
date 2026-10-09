# Connected Platforms

How the skill uses whatever tools you have connected to Claude Code (MCP servers, browser automation, CLIs). Nothing here is required. With zero connections the skill still works: it asks you for numbers and gives you paste-ready copy. Every connection you add lets it read more for itself and, with your yes, make the change for you.

## Contents
- How detection works
- Platform map (read / write / used by)
- Skool facts worth knowing before reading or writing
- Write protocol
- Connection table format (stored in your profile)

## How detection works

At `/skool-platinum onboard` (and at the start of `optimize`), Claude looks at the tools available in the current session and groups them by platform using the tool names. Examples: tools whose names contain `skool` → Skool; `stripe` → Stripe; `ghl` / `highlevel` / `kit` / `convertkit` / `mailchimp` / `gmail` → email; `meta` / `facebook` → Meta ads; `youtube` / `vidiq` → YouTube; `instagram` → Instagram; `manychat` → ManyChat; `ga4` / `analytics` → analytics; `calendar` → calendar; `claude-in-chrome` / `playwright` → browser. If a tool family is deferred, load it with ToolSearch before calling it. CLI tools count too when they are installed and logged in (for example `gh`, `stripe`, `gws`).

Detection is a guess from names. Confirm the list with the user before relying on it, then save it in the profile's connection table.

## Platform map

| Platform | What the skill reads | What it can change (only with a yes per item) | Used by |
|---|---|---|---|
| Skool (a Skool MCP server) | Group settings, about text, description, pricing tiers, classroom tree, pinned and recent posts, comments, calendar, members, analytics | Posts, comments, pinned post, classroom pages, about text, description, calendar events, auto-DM | onboard, status, optimize, setup, audit, deliver |
| Skool (browser: Claude in Chrome or Playwright, logged in) | The admin dashboard behind Settings: members, MRR, new MRR, engagement, retention, about-page visitors, signups, conversion, signup sources; Discovery rank and Growth Boost; Pricing tab | Same fields by clicking, only when no Skool API tool exists, one field at a time with a screenshot after | onboard, status, optimize, audit |
| Stripe or another billing tool (only if you sell outside Skool) | MRR, churn, failed payments, plan mix | Nothing. Pricing and refunds are drafted for you to apply | status, optimize, audit |
| Email (Kit, GoHighLevel, Mailchimp, Gmail and similar) | List size, recent campaign opens and clicks | Create a draft or a scheduled campaign for the launch sequence | launch, optimize |
| YouTube (YouTube API, vidIQ) | Subscribers, top videos, descriptions, pinned comments, channel links | Description header lines, pinned comments, channel links | launch, grow, optimize |
| Instagram / TikTok | Followers, bio, link in bio, highlights, recent posts | Bio and link changes (usually by you; the skill drafts them) | launch, grow |
| ManyChat | Keywords, flows | New keyword flow (draft first) | grow |
| Meta Ads | Spend, cost per signup, the pixel you added in Skool Plugins | Pause or budget changes, drafted for your yes | optimize, audit |
| Analytics (GA4, Clarity) | Traffic to any page you send people to before Skool | Nothing | audit, optimize |
| Calendar (Google Calendar or similar) | Upcoming live calls | Kickoff call and live-call events | setup task 6, deliver |
| Docs (Google Docs, Notion) | Nothing required | Save a copy of reports and drafts | any task, on request |

## Skool facts worth knowing before reading or writing

Collected from Platinum lessons, staff answers in the feed, and hands-on use of Skool:
- The dashboard's headline "conversion rate" counts free signups. On a freemium group it flatters you. New MRR is the number that shows whether people upgrade.
- Only recurring revenue counts for Platinum rankings. Annual plans count as one twelfth per month. One-time sales do not count (chunk 09).
- Growth Boost lives in Settings > Discovery. Skool takes a share of revenue from members it brings in; turning it off cuts Skool network traffic sharply (chunks 07, 09).
- The about-page description field has a character cap (about 1,000). Count before you paste.
- Skool posts and comments show markdown symbols as plain text. Use plain text and CAPS for emphasis.
- Classroom page bodies are stored as rich-text JSON, so a page can look empty to a tool that reads a plain "body" field. Check the actual content before saying a page is blank.
- A Meta pixel and Conversions API token can be added in Settings > Plugins, so a paid join can be tracked.

## Write protocol

1. Show a change table: platform, exact location, current value, proposed value, the Platinum source that justifies it.
2. Wait for a yes per row ("yes to 1 and 3" is fine; silence is a no).
3. Make the change with the matching tool.
4. Read it back and show the new value next to the proposed one.
5. Log it in `skool-platinum/TRACKER.md` under Change log with the date.

## Connection table format (stored in your profile)

```
| Platform | Tool or method | Read | Write | Checked |
|---|---|---|---|---|
| Skool | mcp: skool_* | yes | yes | 2026-10-09 |
| Skool dashboard | Claude in Chrome | yes | no | 2026-10-09 |
| Email | Kit API | yes | drafts only | 2026-10-09 |
```
