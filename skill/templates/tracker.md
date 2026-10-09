# Platinum Tracker Template

## Contents
- Template block (fenced)
- Field Documentation
- Section Specifications

Output file: `skool-platinum/TRACKER.md` (created by /skool-platinum onboard, updated by status, optimize and every task that finishes an artifact)

```template
# Platinum Tracker: {group-name}
Updated {YYYY-MM-DD} · Primary group {group-url} · Baseline MRR on Oct 1: {baseline}

## Scoreboard
| Today | Current MRR | Growth since Oct 1 | Next milestone | Due | Gap | Needed per day |
|---|---|---|---|---|---|---|
| {date} | {mrr} | {growth} | +${target} | {due-date} | {gap} | {gap / days left} |

## Milestone ladder (growth counted from Oct 1, timer starts Nov 1)
| Day | Date (confirm on your rankings tab) | Target growth | Status |
|---|---|---|---|
| Launch | as early as possible, before Nov 1 | launched | {todo/done} |
| 30 | 2026-11-30 | +$1,000 | |
| 60 | 2026-12-30 | +$5,000 | |
| 90 | 2027-01-29 | +$10,000 | |
| 120 | 2027-02-28 | +$20,000 | |
| 150 | 2027-03-30 | +$30,000 | |

## Tasks
| # | Task | Platinum source | Status | Due | Output |
|---|---|---|---|---|---|
| S1 | Positioning, deliverables, price | Task 1 lesson, chunks 01-02 | todo | | |
| S2 | About page + about video | Task 2 lesson, chunk 03 | todo | | |
| S3 | Cover image + description | Task 3 lesson, chunk 03 | todo | | |
| S4 | Start Here post | Task 4 lesson, chunk 04 | todo | | |
| S5 | Classroom plan (MVP) | Task 5 lesson, chunk 04 | todo | | |
| S6 | Kickoff call scheduled | Task 6 lesson, chunk 04 | todo | | |
| L1 | Socials point at the about page | "Add Your Socials" lesson, chunk 09 | todo | | |
| L2 | 5-day tease | "Teasing the Launch" lesson, chunk 05 | todo | | |
| L3 | Launch posts + bulk YouTube descriptions | Launch folder, chunk 05 | todo | | |
| L4 | Launch email | "Email Launch Copy" lesson, chunk 05 | todo | | |
| D1 | Daily owner flow running | Delivery folder, chunk 06 | todo | | |
| D2 | Live call cadence set | "Live Calls" lesson, chunk 06 | todo | | |
| G1 | CTA in every piece of content | "How to CTA" lesson, chunk 07 | todo | | |
| G2 | IG + YouTube profile checklists pass | Promotion folder, chunk 07 | todo | | |
| G3 | Growth Boost decision | Bonus lesson, chunks 07, 09 | todo | | |

## This week (max 3)
1. {highest-leverage open task}
2. 
3. 

## Change log
| Date | Platform | Change | Approved | Read back |
|---|---|---|---|---|
```

## Field Documentation
| Field | Type | Notes |
|---|---|---|
| {baseline} | number | MRR on Oct 1; ranking growth is counted from here (chunk 09) |
| Growth | number | New MRR minus churned MRR since Oct 1; annual plans count as price / 12; one-time sales do not count |
| Dates | date | Day N = Nov 1 + (N - 1) days; the rankings tab is the authority |
| Status | enum | todo / doing / done / skipped (with reason) |

## Section Specifications
- **Scoreboard first**: the one number that decides elimination is growth since Oct 1 vs the next target.
- **This week**: never more than 3 items, picked by impact on MRR growth.
- **Change log**: every write the skill made on any platform, with read-back result.
