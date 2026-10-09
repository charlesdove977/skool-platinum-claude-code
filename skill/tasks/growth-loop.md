## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. map_current_loop · 2. score_profiles · 3. write_cta_system · 4. review_and_deliver
- output · acceptance-criteria

<purpose>
Build the Platinum promotion system for a group: the content-to-CTA-to-community growth loop, CTA scripts per platform, Instagram and YouTube profile checklists scored against the owner's real profiles, and ManyChat keyword and TikTok Live plans.
</purpose>

<user-story>
As a Platinum member, I want my content to reliably feed new members into my Skool, so that growth comes from a repeatable loop instead of one-off launches.
</user-story>

<when-to-use>
- The user runs /skool-platinum grow
- New-member flow is flat while content output is steady
- Adding a new channel (TikTok Live, ManyChat)
</when-to-use>

<context>
@context/my-skool-profile.md
</context>

<references>
@frameworks/chunks/07-promotion-and-growth-loop.md (loop, CTA, checklists, TikTok Live, ManyChat, Growth Boost)
@frameworks/chunks/08-mentor-playbooks-100k.md (traffic models, Samuel G TikTok Live)
@context/competitor-landscape.md (how competitors CTA into their groups)
</references>

<steps>

<step name="map_current_loop" priority="first">
Ask which group and which channels to include. Then gather (read-only, public pages or the owner's numbers): YouTube channel header/links/description CTA, IG bio + link + highlights, TikTok bio, existing ManyChat keywords, current CTA wording in recent videos/posts. Draw the current loop and mark where it leaks.

**Wait for the user to confirm the map.**
</step>

<step name="score_profiles">
Score the owner's IG profile and YouTube channel against the checklists in chunk 07, item by item, with a fix for each fail.
</step>

<step name="write_cta_system">
Write: 3 CTA scripts per platform (spoken, caption, pinned comment), a ManyChat keyword flow (keyword, reply, follow-up, Skool link framing), and a TikTok Live run-of-show if TikTok is in scope. Note Growth Boost eligibility and how to use it from chunk 07. Every CTA points to the about page (the single-link rule in chunk 07) and names the transformation, never a bare link.
</step>

<step name="review_and_deliver">
Save to `skool-platinum/growth/{group-slug}/{YYYY-MM-DD}.md`. Show the loop diagram, profile scorecards, and the CTA pack. Profile or bio changes on any platform need the owner's explicit yes.
</step>

</steps>

<output>
`skool-platinum/growth/{group-slug}/{YYYY-MM-DD}.md` with loop map, profile scorecards, CTA pack, ManyChat flow, TikTok Live plan.
</output>

<acceptance-criteria>
- [ ] Current loop mapped with leak points named
- [ ] Both profile checklists scored item by item
- [ ] CTA scripts for every in-scope platform
- [ ] No profile changes made without approval
</acceptance-criteria>
