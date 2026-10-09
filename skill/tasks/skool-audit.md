## Contents
- purpose · user-story · when-to-use · context · references
- Steps: 1. scope · 2. collect_evidence · 3. score_each_area · 4. prioritize · 5. render_pdf · 6. review_and_deliver
- output · acceptance-criteria

<purpose>
Audit one or all of the owner's Skool groups against every Platinum framework and the competitor set, score each area, and ship a clean master-class PDF of what to improve, with sources and links for every recommendation.
</purpose>

<user-story>
As a Platinum member, I want my Skool graded against the Platinum playbook and real competitors with prioritized fixes and sources, so that I know exactly what to change first and why.
</user-story>

<when-to-use>
- The user runs /skool-platinum audit, "audit my skool", "analyze my skool"
- Before a relaunch, price change or ad push
- Monthly health check (re-run and compare with the previous audit)
</when-to-use>

<context>
@checklists/audit-rubric.md
@context/my-skool-profile.md
@context/competitor-landscape.md
</context>

<references>
@frameworks/chunks/01-offer-and-positioning.md through @frameworks/chunks/10-community-field-notes.md (load each one when its rubric area is scored)
@templates/audit-report.md (report structure)
</references>

<steps>

<step name="scope" priority="first">
Copy this checklist into your reply and tick it off as you go (order matters):
```
- [ ] 1 scope confirmed
- [ ] 2 evidence collected (API + dashboards + profiles)
- [ ] 3 every rubric area scored with a source
- [ ] 4 top 5 fixes pressure-tested
- [ ] 5 PDF rendered and every page checked
```

Ask: which group(s) (default: every group in the profile, with the primary Platinum group first), and whether to refresh live data (default yes). Ask for any numbers the API cannot read (about-page conversion, ad spend, churn) or accept "not available".

**Wait for response.**
</step>

<step name="collect_evidence">
Read-only only. For each group, refresh with the connected Skool tool (context/connected-platforms.md): settings, about text + video, cover, description, membership products/price, gates/questions, auto-DM, levels, labels, classroom tree, pinned + last 30 posts, calendar, analytics/stats. Save raw evidence to `skool-platinum/audits/{YYYY-MM-DD}/evidence/`. Download the cover and about-page images.

If context/competitor-landscape.md is older than 30 days, refresh the top competitors' public about pages (browser User-Agent, 1 second between requests).
</step>

<step name="score_each_area">
Score every rubric area in checklists/audit-rubric.md from 0 to 5 using the matching chunk as the standard. For each area record: current state (evidence quote or number), the Platinum standard (chunk + lesson/transcript source), the gap, the fix, the effort (S/M/L), and the expected impact (H/M/L). Use competitor examples by name where they show the standard done well. Every claim carries a source: Skool URL, lesson file, transcript [h:mm:ss], or competitor URL.

Never fabricate numbers. Mark unknowns as "not visible via API". If any area has no source, return to collect_evidence for it before scoring.
</step>

<step name="prioritize">
Build the action plan: Quick wins (high impact, small effort) first, then 30-day and 90-day moves. Tie each to a revenue lever (conversion, price, retention, traffic). Include rewritten copy for the top fixes (positioning line, description, about-page draft, Start Here post) so the PDF is directly usable.

Pressure-test the top 5 recommendations: for each, write the strongest objection and keep it only if it survives.
</step>

<step name="render_pdf">
Install for rendering (skip if present): `pip3 install weasyprint markdown`, `brew install pango poppler` (pango for weasyprint, poppler for `pdftoppm`). Run weasyprint with `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` or it cannot find libgobject.

Write the report markdown with templates/audit-report.md to `skool-platinum/audits/{YYYY-MM-DD}/skool-audit.md`, then render a PDF to the same folder (weasyprint or reportlab).

PDF rules: the owner's logo at the top of every page (logo path and brand colors from the Guardrails section of the profile; if none, a plain text header), light background, one accent color for headers and dividers, footer on every page with company, site and page number, never a blank page, clean and easy to read (one idea per section, scorecards as tables, generous white space, a table of contents, clickable source links).

Render every page to PNG and visually check every page for blank pages, overflow, orphaned headings and broken tables. If any page fails, fix the markdown or CSS and return to the start of this step; deliver only when all pages pass.
</step>

<step name="review_and_deliver">
Present the scorecard table, the top 5 fixes, and the PDF path. Ask which fixes the user wants executed next; route copy fixes to /skool-platinum setup and launch work to /skool-platinum launch. Any write to Skool needs a per-write yes.
</step>

</steps>

<output>
`skool-platinum/audits/{YYYY-MM-DD}/` containing `evidence/`, `skool-audit.md` and `skool-audit-master-class.pdf`.
</output>

<acceptance-criteria>
- [ ] Every rubric area scored 0 to 5 with evidence and a Platinum source
- [ ] Every recommendation has a source link or file reference
- [ ] No invented numbers; unknowns labelled
- [ ] Top 5 recommendations pressure-tested
- [ ] PDF follows the PDF rules above and was visually checked page by page
- [ ] No writes to Skool
</acceptance-criteria>
