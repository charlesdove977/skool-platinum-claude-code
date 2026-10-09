## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. pick_group_and_scope · 2. load_real_state · 3. run_task_1 · 4. run_task_2_and_3 · 5. run_task_4_to_6 · 6. review_and_deliver
- output · acceptance-criteria

<purpose>
Walk one of the owner's Skool groups (from context/my-skool-profile.md) through the 6 Platinum setup tasks and draft every artifact (positioning statement, deliverables, price, about page, group description, cover brief, Start Here post, classroom plan, kickoff call) from his real data, graded against the Platinum checklists.
</purpose>

<user-story>
As a Skool owner in the Platinum cohort, I want each setup task drafted from my real group data and scored against the Platinum standard, so that I can paste finished copy into Skool instead of starting from a blank doc.
</user-story>

<when-to-use>
- The user runs /skool-platinum setup or names a single task ("do task 2", "write my about page")
- A group is relaunching, repositioning or migrating from another platform
- After an audit flags setup gaps
</when-to-use>

<context>
@context/my-skool-profile.md
@checklists/setup-complete.md
</context>

<references>
@frameworks/chunks/01-offer-and-positioning.md (tasks 1a, 1b)
@frameworks/chunks/02-pricing-and-revenue-math.md (task 1c)
@frameworks/chunks/03-about-page-and-cover-image.md (tasks 2, 3)
@frameworks/chunks/04-onboarding-start-here-and-classroom.md (tasks 4, 5, 6, migration)
@context/competitor-landscape.md (positioning and price sanity checks)
@templates/about-page.md · @templates/start-here-post.md · @checklists/about-page-quality.md
</references>

<steps>

<step name="pick_group_and_scope" priority="first">
Copy this checklist into your reply and tick it off as you go:
```
- [ ] Task 1 positioning, deliverables, price
- [ ] Task 2 about page (+ video outline)
- [ ] Task 3 description + cover brief
- [ ] Task 4 Start Here post
- [ ] Task 5 classroom plan
- [ ] Task 6 kickoff call
- [ ] setup-complete checklist all pass
```

Ask, in one batch:
1. Which group (from the Groups table in context/my-skool-profile.md)?
2. Run all 6 tasks, or a single task (1 positioning/deliverables/pricing, 2 about page, 3 cover + description, 4 Start Here post, 5 classroom plan, 6 kickoff call)?
3. Is this a fresh setup, a reposition, or a migration from another platform?

**Wait for response.**
</step>

<step name="load_real_state">
Read context/my-skool-profile.md for the chosen group. If it is older than 14 days or missing a field the task needs, pull fresh read-only data with the connected Skool tool (context/connected-platforms.md) (group settings, about text, membership products, classroom tree, pinned posts, stats). Never write to Skool in this task.

Ask whether the user already ran the Platinum Setup Assistant GPT (lesson "Platinum Setup Assistant"). If they paste its draft positioning, description or about copy, start from that draft rather than from zero, and say so.

Show the user a 5-line "current state" summary (current positioning line, price, about-page length, classroom count, Start Here post yes/no) before drafting.
</step>

<step name="run_task_1">
Task 1: positioning, deliverables, price (load chunks 01 and 02).
1. Answer the 4 positioning questions (who, outcome, how, proof) from real data; ask only for what is missing. Proof must be real (members, wins, revenue, client results): never invent it.
2. Draft 3 positioning statements in the `[group] helps [who] to [outcome] by [method]` shape, ranked by specificity. Run the generic-statement test from chunk 01 on each.
3. Draft deliverable lines as `[what is inside] - [why it matters to them]`, starting with the 3 Skool defaults (live Q&A, member map, community) and adding real assets from the classroom tree.
4. Price: place the group in its niche band, apply the past-offer rule, propose monthly + annual (20 to 40 percent annual discount band) and show the MRR math to a stated goal. Flag a founding-rate option if relaunching.

**Wait for the user to pick a statement, edit deliverables, and confirm price.**
</step>

<step name="run_task_2_and_3">
Task 2 + 3: about page, description, cover (load chunk 03, templates/about-page.md, checklists/about-page-quality.md).
1. Draft the about page in the what / who / why structure with short bullets, deliverables, and real testimonials only (pull from wins posts if available; otherwise leave a marked slot).
2. Draft a 2 to 5 minute about-video script outline.
3. Draft the group description (Skool's short description field) from the chosen positioning line.
4. Write a cover-image brief: headline benefit, niche signal, the owner's real face photo (the cover examples in chunk 03 mostly show the creator), and the 1 to 2 second test. Do not generate the image here; hand the brief to whatever image tool the user prefers.
5. Score the about draft against checklists/about-page-quality.md and fix every fail before showing it.

**Wait for approval or edits.**
</step>

<step name="run_task_4_to_6">
Tasks 4 to 6 (load chunk 04, templates/start-here-post.md).
1. Start Here post: greeting, reminder of why they joined, intro-post ask, first action. Match the tone of the group.
2. Classroom plan: map the current classroom tree onto the 3 uses (course content, recorded calls, resources); propose the MVP structure and what NOT to build before launch.
3. Kickoff call: date options, a 45 to 60 minute agenda, and the calendar/event text.

**Wait for approval or edits.**
</step>

<step name="review_and_deliver">
1. Run checklists/setup-complete.md and show the pass/fail table. Any fail: return to the task step that owns it (run_task_1, run_task_2_and_3 or run_task_4_to_6), fix, and re-run the checklist. When a fail reveals a rule the checklist lacks, propose the new line at the end of the run for the user to approve.
2. Save every approved artifact to `skool-platinum/setup/{group-slug}/{YYYY-MM-DD}/` as one markdown file per task.
3. Ask whether the user wants any artifact written into Skool. If yes, list each exact write (page, field, post) and wait for an explicit yes per write before using the connected Skool tool (context/connected-platforms.md), following the Safety rules in SKILL.md (read back after every write).
</step>

</steps>

<output>
One folder per run at `skool-platinum/setup/{group-slug}/{YYYY-MM-DD}/` containing `01-positioning-deliverables-price.md`, `02-about-page.md`, `03-cover-and-description.md`, `04-start-here-post.md`, `05-classroom-plan.md`, `06-kickoff-call.md`, plus `checklist.md` with the setup-complete results.
</output>

<acceptance-criteria>
- [ ] Every draft is grounded in real group data or a stated answer from the user, with no invented proof
- [ ] Positioning statement passes the specificity test from chunk 01
- [ ] Price sits inside the niche band or the deviation is justified in writing
- [ ] About page passes every item in checklists/about-page-quality.md
- [ ] setup-complete checklist shown with pass/fail per task
- [ ] Nothing written to Skool without an explicit per-write yes
</acceptance-criteria>
