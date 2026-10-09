## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. read_the_room · 2. set_the_flow · 3. draft_week_of_posts · 4. review_and_deliver
- output · acceptance-criteria

<purpose>
Run the Platinum delivery system on a live group: read which engagement phase it is in, set the owner's daily owner flow, plan live calls, and draft a week of high-engagement posts from the real feed.
</purpose>

<user-story>
As a Platinum member, I want a daily flow and a week of posts matched to where my community actually is, so that members stay active and churn stays low without me guessing what to post.
</user-story>

<when-to-use>
- The user runs /skool-platinum deliver
- Engagement or post volume drops, or churn rises
- First 30 days after a launch
</when-to-use>

<context>
@context/my-skool-profile.md
</context>

<references>
@frameworks/chunks/06-delivery-and-engagement.md (daily flow, live calls, 3 phases, post ideas)
@frameworks/chunks/10-community-field-notes.md (what real members asked and responded to)
@frameworks/chunks/08-mentor-playbooks-100k.md (retention tactics from $100k owners)
</references>

<steps>

<step name="read_the_room" priority="first">
Ask which group, then pull read-only: last 30 posts with likes/comments, member count trend, online count, unanswered posts, calendar events. Classify the group into one of the 3 engagement phases from chunk 06 and show the evidence.

**Wait for the user to confirm the read.**
</step>

<step name="set_the_flow">
Write the owner's daily owner flow for this phase (time blocks, what to answer, who to welcome, what to post) and the live-call cadence with an agenda template. Keep it realistic for a solo operator; mark which pieces can be delegated or automated.
</step>

<step name="draft_week_of_posts">
Draft 7 posts using the high-engagement formats from chunk 06, each tied to a real topic from the feed or classroom. For each: category label, title, body, and the engagement mechanic (question, poll, win share, challenge). Voice rules apply.
</step>

<step name="review_and_deliver">
Show the flow and the post calendar. Save to `skool-platinum/delivery/{group-slug}/{YYYY-MM-DD}.md`. Posting needs per-post approval and follows the Safety rules in SKILL.md.
</step>

</steps>

<output>
`skool-platinum/delivery/{group-slug}/{YYYY-MM-DD}.md` with phase read, daily flow, live-call plan and 7 draft posts.
</output>

<acceptance-criteria>
- [ ] Engagement phase backed by real feed numbers
- [ ] Daily flow fits a solo operator and names delegable parts
- [ ] 7 posts drafted, each with a distinct engagement mechanic
- [ ] No posts published without approval
</acceptance-criteria>
