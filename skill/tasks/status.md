## Contents
- purpose · user-story · when-to-use · context
- Steps: 1. refresh_numbers · 2. update_tracker · 3. report
- output · acceptance-criteria

<purpose>
Task manager for the Platinum run. Refresh the MRR numbers, update the tracker, and tell the owner exactly where they stand against the next milestone and what to do this week.
</purpose>

<user-story>
As a Platinum member, I want one command that tells me what is done, what is next and how far I am from the next cut, so that I spend this week on the thing that moves MRR.
</user-story>

<when-to-use>
- The user runs /skool-platinum status, or asks "what's next", "where am I", "am I on track"
- Start of each week
- After any other task finishes an artifact (mark it done)
</when-to-use>

<context>
@context/my-skool-profile.md
@frameworks/chunks/09-platinum-program-and-proof.md (milestones and counting rules)
@frameworks/chunks/02-pricing-and-revenue-math.md (traffic and conversion math)
</context>

<steps>

<step name="refresh_numbers" priority="first">
If `skool-platinum/TRACKER.md` does not exist, route to tasks/onboard.md.

Read-only. Pull current MRR, new MRR, churned MRR (if visible), paying members, about-page visitors and signups for the last 7 and 30 days through the connected Skool tool or browser (context/connected-platforms.md). If nothing is connected, ask the user for current MRR and paying members only.
</step>

<step name="update_tracker">
1. Recompute the scoreboard: growth since Oct 1 (annual plans count as price / 12, one-time sales do not count), next milestone, days left, gap, gap per day, and the paying members needed at the current price to close it.
2. Mark tasks done when their output file exists in `skool-platinum/` or the change is visible live; link the evidence.
3. Re-pick "This week" (max 3), ranked by expected MRR impact before the next cut. Use the decision tree in frameworks/platinum-october.md to route each to a command.
</step>

<step name="report">
Show, in this order:
1. Scoreboard row.
2. One sentence: on track / behind / ahead, and by how much per day.
3. "This week" with the command for each.
4. Anything blocked and what unblocks it.

If behind: name the single biggest lever from the numbers (traffic, about-page conversion, price, churn) using the traffic math in chunk 02 and the field-notes answers in chunk 10, and offer /skool-platinum optimize.
</step>

</steps>

<output>
Updated `skool-platinum/TRACKER.md` and a short status report in the conversation.
</output>

<acceptance-criteria>
- [ ] Scoreboard uses real numbers from a tool or the user, with the date read
- [ ] Growth counted by the Platinum rules (recurring only, annual / 12)
- [ ] Every task marked done links to evidence
- [ ] No more than 3 "This week" items, each with a command
- [ ] No writes to any platform
</acceptance-criteria>
