## Contents
- purpose · user-story · when-to-use · references
- Steps: 1. route_question · 2. search_raw_source · 3. answer_with_sources
- output · acceptance-criteria

<purpose>
Answer any free-form question from the Platinum knowledge base (chunks first, raw source second) with a direct answer and checkable sources.
</purpose>

<user-story>
As a Platinum member, I want to ask "what did Platinum say about X" and get a straight answer with the lesson, call timestamp or post behind it, so that I can act without rewatching hours of calls.
</user-story>

<when-to-use>
- The user runs /skool-platinum ask, or asks any Platinum, Skool-growth or mentor question
- Another task needs a fact that is not in the loaded chunk
</when-to-use>

<references>
@frameworks/platinum-october.md (decision tree to pick the chunk)
@context/source-map.md (raw source locations for grep fallback)
</references>

<steps>

<step name="route_question" priority="first">
Use the decision tree in frameworks/platinum-october.md to pick 1 to 2 chunks and load them. If the answer is there, go to answer_with_sources.
</step>

<step name="search_raw_source">
If the chunks do not cover it, grep the raw source listed in context/source-map.md (transcripts first for mentor questions, community/ for member problems, classroom/ for program rules). Read the surrounding passage, not just the matching line.
</step>

<step name="answer_with_sources">
Answer in 1 to 3 short paragraphs or a table: the recommendation first, then the reasoning. Cite each claim as `lesson file`, `transcript file [h:mm:ss]` or `post file (date)`. If mentors disagree, show both positions. If nothing in the source covers it, say so plainly and do not fill the gap with outside guesses presented as Platinum advice.

If the answer applies to one of the owner's groups, end with one concrete next action and the task that executes it.
</step>

</steps>

<output>
Inline answer in the conversation with source citations. No file unless the user asks to save it.
</output>

<acceptance-criteria>
- [ ] Every claim cited to a lesson, transcript timestamp or post
- [ ] Gaps in the source stated plainly, not invented
- [ ] Actionable next step when the question concerns the owner's groups
</acceptance-criteria>
