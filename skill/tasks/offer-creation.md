## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. frame_the_session · 2. steps_one_to_four · 3. pressure_test · 4. finalize_and_validate
- output · acceptance-criteria

<purpose>
Run the 6-step Skool Offer Creation flow interactively (accomplishments, transformation, best-fit member, exact result, pressure test, final offer + validation) and land one offer statement the user can put on their group.
</purpose>

<user-story>
As a Platinum member, I want to be interviewed through the Platinum offer flow using my real accomplishments and audience, so that my Skool offer is specific, believable and pressure-tested before I rebuild the about page or price around it.
</user-story>

<when-to-use>
- The user runs /skool-platinum offer
- Audit or about-page work shows the outcome is vague or the offer is not converting (the "Offer not converting?" lesson routes here)
- Before repositioning any group
</when-to-use>

<context>
source/offer-creation-prompt.md (the full 6-step Platinum offer rule set; follow its rules exactly)
@context/my-skool-profile.md
</context>

<references>
@frameworks/chunks/01-offer-and-positioning.md (specificity test, positioning formula, examples)
@frameworks/chunks/08-mentor-playbooks-100k.md (when the user asks how a $100k owner framed their offer)
@context/competitor-landscape.md (differentiation in step 5)
@templates/offer-snapshot.md (final step output)
</references>

<steps>

<step name="frame_the_session" priority="first">
Read the saved offer-creation prompt fully and adopt its operating rules for the whole task: one transformation, the `I help [person] achieve [result] by [timeframe or method]` target, small question batches (max 3), multiple choice where possible, no moving on without an answer, never call the community a course, never invent proof, no modules/pricing/bonuses in this flow.

Pre-fill what is already known from context/my-skool-profile.md (their wins, audience, current positioning) and show it as "what I already know, correct me".

Start every reply with `Step X of 6 - [name]` and end completed steps with decided / unresolved / next.

Ask the Step 1 question with examples.

**Wait for response.**
</step>

<step name="steps_one_to_four">
Run Steps 1 to 4 exactly as the saved prompt defines them:
1. Accomplishments: summarize, pick the most teachable, ask for proof.
2. Transformations: 3 to 5 before/after options with who, result, qualification, strength; the user chooses.
3. Best-fit member: situation, attempts, struggle, stage; ask for one real example person if vague; offer 3 polished member descriptions.
4. Exact result: push vague outcomes into observable ones; offer 3 increasingly specific result versions.

Use chunk 01 examples to show what "specific enough" looks like. **Wait for response after every step.**
</step>

<step name="pressure_test">
Step 5: ask the pressure questions in batches of 3, then fill the rating table (pain, urgency, result clarity, ability to pay, credibility, differentiation) with an honest one-line reason per rating. Use context/competitor-landscape.md to judge differentiation against real competitors by name. If any rating is weak, propose concrete fixes (narrow audience, sharper result, different timeframe, better-supported transformation).

**Do not advance until the user agrees the offer is strong enough.**
</step>

<step name="finalize_and_validate">
Step 6: write 3 versions (simple, emotional, specific), let the user pick or merge, then fill templates/offer-snapshot.md (who, problem, result, timeframe/method, why different, final statement, 7 to 14 day quick win) plus 3 validation actions.

Save to `skool-platinum/setup/{group-slug}/{YYYY-MM-DD}/offer-snapshot.md`. Close with `Progress: 6/6 steps complete` and offer to hand the statement to /skool-platinum setup task 1.
</step>

</steps>

<output>
`offer-snapshot.md` in `skool-platinum/setup/{group-slug}/{YYYY-MM-DD}/`, following templates/offer-snapshot.md.
</output>

<acceptance-criteria>
- [ ] All 6 steps run in order with a wait at every step
- [ ] Every response starts with the step header
- [ ] No proof, numbers or audience details invented
- [ ] Rating table filled with honest reasons; weak ratings got concrete fixes
- [ ] Final statement fits the `I help [person] achieve [result] by [timeframe or method]` shape
- [ ] Offer snapshot saved and approved by the user
</acceptance-criteria>
