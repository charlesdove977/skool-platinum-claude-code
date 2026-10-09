## Contents
- purpose · user-story · when-to-use · context
- Steps: 1. preflight · 2. run_pull · 3. scrub · 4. diff_and_flag
- output · acceptance-criteria

<purpose>
Re-pull the Platinum (October) classrooms, video transcripts, community posts, images and linked docs read-only with the member's own Skool login, pseudonymize the community feed, then flag which framework chunks need updating.
</purpose>

<user-story>
As a Platinum member, I want new Platinum lessons, calls and posts pulled into the knowledge base in one command, so that the skill never goes stale during the cohort.
</user-story>

<when-to-use>
- The user runs /skool-platinum refresh
- A new mentor call, lesson or major community thread has dropped
</when-to-use>

<context>
@context/source-map.md
@frameworks/platinum-october-chunks.md
</context>

<steps>

<step name="preflight" priority="first">
Copy this checklist into your reply and tick it off as you go:
```
- [ ] tools installed, cookie jar found
- [ ] classroom + media + feed pulled, zero FAILED lines
- [ ] feed scrubbed, leak check clean
- [ ] change list mapped to chunks, edits approved
```

Install what the scripts need (skip any already present):
- `brew install ffmpeg yt-dlp` (stream audio + YouTube/Loom captions)
- `pip3 install --user faster-whisper` (Whisper fallback; run media.py WITHOUT `-I` so user site-packages load)
- Python 3 standard library covers scrape.py, posts.py, comments.py, render.py, tree.py, scrub.py

Skool login: export your skool.com cookies in Netscape format (any "cookies.txt" browser extension, while logged in) to `~/.skool_cookies.txt`, or point `SKOOL_COOKIES` at the file. Never commit or share that file; it is your login.

Tell the user this is read-only (GET requests to Skool, Mux and YouTube only) and takes 5 to 15 minutes.
</step>

<step name="run_pull">
The scripts write caches next to themselves, so copy `scripts/` into a fresh scratch folder and run there, with `PLATINUM_OUT` pointing at this skill's `source/` folder (absolute path):
```
export PLATINUM_OUT="<absolute path to this skill>/source"
export SKOOL_COOKIES="$HOME/.skool_cookies.txt"
```
1. Fetch each classroom root page into `plat/{root}.html` (curl `-L` with the cookie jar and a browser User-Agent) and run `python3 -I tree.py {roots}` to cache the trees. Roots: `5fab3dee` (Start Here), `3c0d8b16` ($100k/mo Interviews), `6ba34c4d` (Need Help?), plus any new root on `skool.com/platinum-october/classroom`.
2. `python3 -I scrape.py 5fab3dee 3c0d8b16 6ba34c4d` (plus new roots).
3. `python3 media.py` (no `-I`). Captions first, Whisper fallback. Mux streams need the skool.com Referer header (already set).
4. `python3 -I posts.py`, then `python3 -I comments.py`, then `python3 -I render.py`.
Existing transcripts and images are skipped, so only new items download. Any log line containing FAILED: retry that item once, then report it.
</step>

<step name="scrub">
The community feed holds other members' names, links and photos. Before using or sharing it:
1. `python3 -I scrub.py <scratch>/posts "$PLATINUM_OUT/community"` (replaces member names with stable `Member xxxx` pseudonyms, strips profile ids, handles, emails, phones and non-allowlisted links; keeps Skool staff, Hormozi and the mentors).
2. Delete `$PLATINUM_OUT/community/images/` (member screenshots).
3. Leak check: `python3 -I leak_check.py <scratch>/posts/_private_roster.json "<absolute path to this skill>"` must print `0 hits`. If not, add the missed name pattern to scrub.py and return to step 1 of this scrub.
`_private_roster.json` stays in the scratch folder. Never copy it into the skill.
</step>

<step name="diff_and_flag">
List new or changed lessons, transcripts and posts since the last pull (compare file lists and the `pulled:` dates). Map each to the chunk it belongs to using frameworks/platinum-october-chunks.md and propose specific updates as dated "Update {date}" or "Field update {date}" lines, citing the source file. Apply them only after the user approves, then run the leak check again.
</step>

</steps>

<output>
Updated `source/` inside this skill, scrubbed, plus a change list with the chunks that need updating.
</output>

<acceptance-criteria>
- [ ] Pull is read-only
- [ ] Zero FAILED lines left in the logs, or failures reported
- [ ] Community feed scrubbed and leak check prints 0 hits
- [ ] Change list maps every new item to a chunk
- [ ] Chunk edits applied only after approval
</acceptance-criteria>
