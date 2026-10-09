## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. read_live · 2. find_the_lever · 3. propose_changes · 4. apply_approved · 5. log_and_schedule
- output · acceptance-criteria

<purpose>
The weekly optimize pass. Read the group's live numbers and surfaces through every connected platform, compare them with the Platinum standards, propose a short list of specific changes with sources, and apply the ones the owner approves through the connected tools, reading each one back.
</purpose>

<user-story>
As a Platinum member with my platforms connected to Claude, I want the skill to look at my real data, tell me what to change, and make the changes I approve, so that I am optimizing every week instead of guessing.
</user-story>

<when-to-use>
- The user runs /skool-platinum optimize
- Status shows the group is behind the milestone pace
- After a launch, a price change, or a traffic spike
</when-to-use>

<context>
@context/my-skool-profile.md
@context/connected-platforms.md
@checklists/audit-rubric.md
</context>

<references>
@frameworks/chunks/02-pricing-and-revenue-math.md (traffic and conversion math, retention math)
@frameworks/chunks/03-about-page-and-cover-image.md (change-one-thing testing loop)
@frameworks/chunks/06-delivery-and-engagement.md (churn diagnosis, engagement phases)
@frameworks/chunks/07-promotion-and-growth-loop.md (CTA test matrix, Growth Boost)
@frameworks/chunks/10-community-field-notes.md (staff answers to the same problems)
</references>

<steps>

<step name="read_live" priority="first">
Copy this checklist into your reply and tick it off as you go:
```
- [ ] live data read (sources listed)
- [ ] one lever chosen with numbers
- [ ] change table shown
- [ ] approved changes applied and read back
- [ ] tracker + change log updated
```

Read-only, from every connected platform (skip what is not connected and say so):
- Skool: MRR, new and churned MRR, about-page visitors → signups (7 and 30 days), signup sources, engagement, retention, unanswered posts, last 14 days of posts with likes and comments, the about text, description, pricing card, Start Here post, calendar.
- Traffic: YouTube and Instagram reach and where the CTA points; email list and last campaign clicks; ad spend and cost per paid signup if ads run.
Compare with the previous `skool-platinum/optimize/` file if one exists and show the deltas.
</step>

<step name="find_the_lever">
Run the funnel math from chunk 02: visitors × about-page conversion × paid share × price, minus churn. Name the ONE stage that most limits MRR growth this week and show the numbers. Use the change-one-thing loop from chunk 03: change one variable per week so the result can be read.
</step>

<step name="propose_changes">
Propose at most 5 changes, all aimed at the chosen lever, as a table: # · platform · exact location · current value · proposed value · Platinum source (lesson, transcript [h:mm:ss] or post) · expected effect. Include ready-to-paste copy for every text change. Changes the skill cannot make (no tool connected, or a payment setting) are marked "you do this" with click-by-click steps.

Score every copy change against checklists/about-page-quality.md and the voice notes in the profile before showing it.

**Wait for a yes per row.**
</step>

<step name="apply_approved">
For each approved row only: make the change with the connected tool, read it back, and show proposed vs live side by side. If a read-back differs or a call fails, stop that row and report the exact error; do not retry with a different method without asking.
</step>

<step name="log_and_schedule">
1. Append every applied change to the tracker's Change log (date, platform, change, approved, read back).
2. Save the week's read, lever, table and results to `skool-platinum/optimize/{YYYY-MM-DD}.md`.
3. State the metric to check next week and the date to check it.
</step>

</steps>

<output>
`skool-platinum/optimize/{YYYY-MM-DD}.md` plus Change log rows in `skool-platinum/TRACKER.md`, and the approved changes live on the connected platforms.
</output>

<acceptance-criteria>
- [ ] Every number came from a live read or the user, with its source
- [ ] One lever chosen and justified with funnel math
- [ ] Every proposed change cites a Platinum source
- [ ] Only approved rows were applied, each read back
- [ ] Change log and optimize file written
</acceptance-criteria>
