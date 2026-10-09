# Skool Platinum (October) for Claude

A Claude skill for the **Skool Platinum October cohort**. It carries the whole Platinum October classroom, as of **October 9, 2026**, and then runs the program on your own Skool group with you: your tasks, your numbers, your launch.

Built for **Claude Code** first. It also works in **claude.ai chat** (instructions below).

Shared with the cohort with the admin's permission.

---

## What's inside

| Part | What you get |
|---|---|
| The full classroom | All 54 lessons (Start Here, $100k/mo Interviews, Need Help?), every lesson image with text notes, the 5 linked Google Docs/Sheets, and the Skool Offer Creation Prompt |
| Transcripts | 17 video transcripts with timestamps: the 6 mentor calls (Nick Saraev, Oscar Patel, Jade, Josh Madakor, James Lu, Samuel G), the TikTok Live example, the onboarding call, and the lesson videos |
| The community feed | 142 threads and 797 comments from the Platinum feed (Sept 25 to Oct 9), including Hormozi's posts and every Skool staff answer. Other members' names are replaced with pseudonyms (see Privacy) |
| 10 framework chunks | The whole program distilled into 164 frameworks you can act on: offer, pricing, about page, Start Here + classroom, launch, delivery, growth loop, mentor playbooks, program rules, and field notes from the feed |
| 11 commands | Onboarding, a task tracker with the Platinum deadlines, a weekly optimize pass, the 6 setup tasks, offer creation, a full audit with a PDF, launch assets, daily delivery, growth loop, Q&A, and a refresh |

## What it does for you

| Command | What happens |
|---|---|
| `/skool-platinum onboard` | **Start here.** Finds the tools you have connected to Claude, reads your Skool group's real numbers, asks only for what it can't read, and builds your profile, competitor list and Platinum tracker |
| `/skool-platinum status` | Your task manager: what's done, what's next, your MRR growth since Oct 1, and how far you are from the next cut ($1K by Nov 30, then $5K, $10K, $20K, $30K) |
| `/skool-platinum optimize` | Weekly pass: reads your live numbers, finds the one thing holding growth back, proposes up to 5 changes with the Platinum lesson behind each, and makes the ones you approve through your connected tools |
| `/skool-platinum setup` | Walks the 6 setup tasks and drafts everything: positioning, deliverables, price, about page, cover brief, Start Here post, classroom plan, kickoff call |
| `/skool-platinum offer` | The 6-step Skool Offer Creation flow, one step at a time |
| `/skool-platinum audit` | Grades your group against every Platinum framework and your competitors, with a PDF report |
| `/skool-platinum launch` | 5-day tease, launch posts for Instagram and YouTube, the launch email, kickoff call plan |
| `/skool-platinum deliver` | Daily owner flow, live-call plan, and a week of engagement posts from your real feed |
| `/skool-platinum grow` | Growth loop, CTA scripts, profile checklists, ManyChat and TikTok Live plans |
| `/skool-platinum ask` | Ask anything ("what did Mark say about free tiers?") and get an answer with the lesson, timestamp or post it came from |
| `/skool-platinum refresh` | Re-pull new lessons, calls and posts with your own Skool login (Claude Code only) |

## Use it with your other tools

The more you connect to Claude, the more it does for you. Nothing is required.

- **Skool** (a Skool MCP server, or Claude in Chrome / Playwright logged in to your admin dashboard): reads members, MRR, conversion, posts, classroom; can post, edit pages and update your about page
- **Email** (Kit, GoHighLevel, Mailchimp, Gmail): drafts and schedules the launch emails
- **YouTube, Instagram, ManyChat**: checks your CTAs, bio links and keyword flows
- **Meta Ads, GA4, Stripe**: reads spend, traffic and billing to find your biggest lever
- **Google Calendar**: books the kickoff and live calls

**It never changes anything without your yes.** Every change is shown as a table (where, old value, new value, the lesson behind it). It only makes the rows you approve, then reads each one back to prove it landed.

---

## Install in Claude Code

You need [Claude Code](https://claude.com/claude-code) and `git`.

```bash
git clone https://github.com/charlesdove977/skool-platinum-claude-code.git
cd skool-platinum-claude-code
./install.sh
```

That puts the skill in `~/.claude/skills/skool-platinum`, so it works in every project. To install it only for one project, run `./install.sh --project` from that project's folder.

Restart Claude Code, then type:

```
/skool-platinum onboard
```

Everything the skill writes for you (drafts, tracker, audits) goes in a `skool-platinum/` folder inside the folder where you run Claude Code.

**Windows:** run `./install.sh` from Git Bash or WSL, or copy the `skill` folder to `%USERPROFILE%\.claude\skills\skool-platinum` by hand.

**Update later:** `git pull && ./install.sh`. Your filled-in profile and competitor files are kept.

## Install in claude.ai chat

Works on Pro, Max, Team and Enterprise plans.

1. Download **`skool-platinum.zip`** from this repo's [Releases page](https://github.com/charlesdove977/skool-platinum-claude-code/releases/latest). Don't unzip it.
2. On [claude.ai](https://claude.ai), open **Settings > Capabilities** (on some accounts it's called **Features**).
3. Turn on **Code execution and file creation**. Skills need it.
4. Under **Skills**, click **Upload skill** and choose `skool-platinum.zip`.
5. Make sure the toggle next to **skool-platinum** is on.
6. Start a new chat and type: **"Run skool platinum onboard."**

What's different in chat:
- Chat can't save files between conversations. The skill hands you your profile and tracker as files to download. Upload them again (or paste your numbers) when you start a new chat.
- Your connected platforms are the connectors you turn on in claude.ai Settings (Gmail, Google Calendar, Google Drive and others).
- `refresh` only works in Claude Code. In chat, download a newer zip from Releases when one is published.

If your team admin manages skills, they can also add the zip for the whole organization under **Organization settings > Plugins & skills**.

---

## Privacy: what was taken out

- **The person who packaged this:** no profile, numbers, groups, competitor research or drafts. Your own profile starts blank and only fills in on your machine (or in your chat).
- **Other cohort members:** names in the community feed are replaced with stable pseudonyms like `Member 3fa2` (the same person always gets the same tag). Profile IDs, @handles, emails, phone numbers, links to members' own sites, socials and Skool groups, and member post images are removed.
- **Kept as-is:** the classroom lessons, lesson images and transcripts, plus the names of Alex Hormozi, the Skool staff who answer in the feed (Mark N., Claire Q. and team), and the six interviewed mentors.
- **Two feed posts** were deleted by their authors after they were captured. The frameworks still use what they taught, but their text isn't included.

A leak check (`skill/scripts/leak_check.py`) scans every file for every member's name, handle, ID and personal links. This release passes with 0 hits.

## Keep it fresh (Claude Code)

New lessons, calls or posts? Run `/skool-platinum refresh`. It uses **your own** Skool login: export your skool.com cookies (any "cookies.txt" browser extension, while logged in) to `~/.skool_cookies.txt`. The pull only reads. It pseudonymizes the new feed, runs the leak check, and then proposes which frameworks to update. Nothing changes until you approve. Never share your cookie file; it is your login.

## What's in the folders

```
skill/
  SKILL.md        entry point: commands, routing, safety rules
  tasks/          the 11 commands, step by step
  frameworks/     index + 10 framework chunks
  context/        source map, connected-platforms guide, your profile + competitors (blank until onboard)
  templates/      tracker, offer snapshot, about page, Start Here post, launch tease, audit report
  checklists/     setup complete, about-page quality, audit rubric
  scripts/        read-only refresh scripts, scrubber, leak check
  source/         the raw classroom, transcripts, linked docs and community feed
```

## License

Code and skill structure: MIT (see `LICENSE`). Course content in `skill/source/` belongs to its owners (Skool / Skool Platinum) and is shared for Platinum October cohort members with the admin's permission.
