## Contents
- purpose · user-story · when-to-use · context
- Steps: 1. detect_connections · 2. pick_groups · 3. pull_real_numbers · 4. interview_gaps · 5. find_competitors · 6. write_profile_and_tracker
- output · acceptance-criteria

<purpose>
First-run setup. Find out which platforms are connected, pull the owner's real Skool numbers through them, ask only for what is missing, and fill context/my-skool-profile.md, context/competitor-landscape.md and skool-platinum/TRACKER.md, so every other task works from real data.
</purpose>

<user-story>
As a Platinum member, I want the skill to learn my group and my numbers once, from the tools I already connected, so that every draft and every recommendation after this is about my community and not a generic one.
</user-story>

<when-to-use>
- First time the skill runs, or context/my-skool-profile.md still says `status: blank`
- The user runs /skool-platinum onboard
- A new platform was connected and should be added to the connection table
</when-to-use>

<context>
@context/connected-platforms.md
@context/my-skool-profile.md
@templates/tracker.md
@frameworks/chunks/09-platinum-program-and-proof.md (milestone ladder and counting rules)
</context>

<steps>

<step name="detect_connections" priority="first">
Copy this checklist into your reply and tick it off as you go:
```
- [ ] connections detected and confirmed
- [ ] groups picked, primary Platinum group named
- [ ] real numbers pulled (or marked not available)
- [ ] gaps filled by interview
- [ ] competitor set filled
- [ ] profile + tracker written
```

List the tools in this session and group them by platform using context/connected-platforms.md. Load deferred tool families with ToolSearch first. Show the result as the connection table, with Read / Write marked "untested".

Ask the user to confirm, and to name anything connected that you missed (CLIs, browser login).

**Wait for response.**
</step>

<step name="pick_groups">
Ask in one batch:
1. Your Skool group URL(s), and which one is your Platinum group (the one whose MRR counts).
2. Your MRR on Oct 1 (the baseline), if you know it; otherwise we read it from the dashboard or billing history.
3. Have you launched yet? If yes, on what date?

**Wait for response.**
</step>

<step name="pull_real_numbers">
Read-only. For each group, pull what the connected tools allow, in this order, and stop asking the user for anything a tool returned:
1. Skool tool or browser on the admin dashboard: members, paying members, MRR, new MRR (30 days), about-page visitors and signups, signup sources, engagement, retention, price tiers, annual price, free trial on/off, Discovery rank, Growth Boost on/off, affiliate %, classroom roots and page count, calendar events, the pinned Start Here post, last 30 posts.
2. Public about page (no login needed): headline, description, about text, video yes/no, cover image.
3. Social and email tools: YouTube subscribers and where the Skool link sits, Instagram followers and link in bio, email list size.

Mark each Read cell in the connection table "yes" when a call returned data, "failed" with the error otherwise. Never guess a number. Show a short "what I found" table.
</step>

<step name="interview_gaps">
Ask for whatever is still empty, at most 3 questions per batch, multiple choice where possible: current offer in one sentence, guarantee wording, real proof (results with numbers and who), audience and their top problems, voice (paste 2 posts you wrote), guardrails (things the skill must never do for you), brand colors and logo path for the audit PDF.

Compare the about page, description, about video and pricing card. List every place where they promise different things under "Known contradictions to fix".

**Wait for response after each batch.**
</step>

<step name="find_competitors">
Ask for 3 to 5 competitor groups the user already knows, then add the top groups from Skool Discovery for the niche keywords (public about pages only, browser User-Agent, 1 second between requests). Fill context/competitor-landscape.md: top communities, the closest paid benchmarks, the patterns that win, and white space.
</step>

<step name="write_profile_and_tracker">
1. Write context/my-skool-profile.md: fill every section, set `status: filled` and `updated:` to today. Keep it under 150 lines; put long evidence in `skool-platinum/evidence/{date}/`.
2. Create `skool-platinum/TRACKER.md` from templates/tracker.md. Mark tasks already done from the evidence (for example, a pinned Start Here post exists → S4 done, with the post link). Compute the scoreboard: growth since Oct 1, next milestone, days left, gap per day.
3. Pick the 3 highest-leverage open tasks for "This week" and say which command runs each.

Show the scoreboard and "This week". If a needed number is missing, show the scoreboard with "not available" in that cell rather than estimating.
</step>

</steps>

<output>
Filled `context/my-skool-profile.md` and `context/competitor-landscape.md` inside the skill folder, plus `skool-platinum/TRACKER.md` (and `skool-platinum/evidence/{date}/` when evidence was saved) in the working folder.
</output>

<acceptance-criteria>
- [ ] Connection table confirmed by the user, with Read/Write results from real calls
- [ ] Every number in the profile came from a tool call or the user; nothing estimated
- [ ] Primary Platinum group and Oct 1 baseline recorded (or marked not available)
- [ ] Contradictions between about page, video, description and pricing listed
- [ ] Tracker created with the milestone ladder, done tasks marked with evidence, and 3 "This week" items
- [ ] No writes to any platform during onboarding
</acceptance-criteria>
