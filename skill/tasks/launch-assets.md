## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. gather_launch_facts · 2. build_traffic_arsenal · 3. write_assets · 4. review_and_deliver
- output · acceptance-criteria

<purpose>
Produce the full Platinum launch package for a group: 5-day tease drip (IG stories / broadcast channel and YouTube community posts), launch posts for Instagram and YouTube, the bulk YouTube description update, the launch email, and the kickoff call plan.
</purpose>

<user-story>
As a Platinum member, I want every launch asset written from my offer and audience in the Platinum format, so that launch day has eager buyers instead of a cold announcement.
</user-story>

<when-to-use>
- The user runs /skool-platinum launch
- A relaunch, price change, new tier, or founding-rate window is coming
- After setup tasks are approved
</when-to-use>

<context>
@context/my-skool-profile.md
@templates/launch-tease-sequence.md
</context>

<references>
@frameworks/chunks/05-launch-playbook.md (tease drip, focus, traffic arsenal, posts, email)
@frameworks/chunks/07-promotion-and-growth-loop.md (CTA wording)
@frameworks/chunks/08-mentor-playbooks-100k.md (launch stories from $100k owners)
@frameworks/chunks/04-onboarding-start-here-and-classroom.md (kickoff call)
</references>

<steps>

<step name="gather_launch_facts" priority="first">
Copy this checklist into your reply and tick it off as you go:
```
- [ ] facts confirmed (date, offer, price, platform)
- [ ] traffic arsenal ranked
- [ ] 5-day drip · launch posts · bulk description · launch email · kickoff
- [ ] voice check passed on every asset
```

Confirm in one batch: group, launch date, the approved offer statement + 3 deliverables, price and any founding-rate cap, primary platform (the focus lesson says pick one), and which assets to produce (default all).

If no approved offer statement exists, stop and route to /skool-platinum offer first.

**Wait for response.**
</step>

<step name="build_traffic_arsenal">
List every audience asset the user owns (YouTube subs and top videos, IG followers and broadcast channel, email list size, Skool free group size, LinkedIn, TikTok) with real numbers from context or the user. Rank them by expected launch signups using chunk 05. Pick the primary platform and the order of secondary pushes.
</step>

<step name="write_assets">
Write, in the owner's voice (profile Voice section) (no em dashes, none of the banned AI phrases):
1. 5-day tease drip from templates/launch-tease-sequence.md, one version for IG stories/broadcast and one for YouTube community posts.
2. Launch-day posts: IG post + caption + story frames; YouTube community post, pinned comment and a launch video outline if a video is planned.
3. Bulk YouTube description header line (Skool link placement) and the steps to apply it with YouTube's bulk edit.
4. Launch email: subject options (3), body, P.S., following chunk 05's structure.
5. Kickoff call: date, agenda, event description, reminder post.

Every CTA names the transformation and the next step, never a bare link.

Voice check every asset: no em dashes, none of the banned phrases in checklists/about-page-quality.md, no claims beyond the profile's proof. Any fail: rewrite that asset and check again before moving on.
</step>

<step name="review_and_deliver">
Present the assets grouped by day in a launch calendar table. Save to `skool-platinum/launch/{group-slug}/{YYYY-MM-DD}/`. Ask for edits. Posting anywhere (Skool, YouTube, IG, email) needs the owner's explicit yes per item.
</step>

</steps>

<output>
`skool-platinum/launch/{group-slug}/{YYYY-MM-DD}/` with `launch-calendar.md`, `tease-drip.md`, `launch-posts.md`, `launch-email.md`, `kickoff-call.md`.
</output>

<acceptance-criteria>
- [ ] Assets built on an approved offer statement
- [ ] Traffic arsenal ranked with real numbers
- [ ] 5-day drip reveals progressively (audience, pain, deliverable 1, deliverables 2 and 3, doors open)
- [ ] Voice rules respected (no em dashes, no banned phrases)
- [ ] Nothing posted without per-item approval
</acceptance-criteria>
