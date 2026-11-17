---
description: Knowledge hygiene. Merge duplicates, retire stale entries, keep the index short.
---
Review knowledge/ and CLAUDE.md.

1. Find duplicates and overlapping learnings. Propose merges.
2. Find entries that contradict the current code (check with grep). Propose retiring them.
3. Find learnings with `seen: 1` older than 90 days. Propose retiring them.
4. Find CLAUDE.md rules no longer needed. Propose removal.
5. Check that knowledge/INDEX.md matches the files.

Present proposals, apply only what the user accepts. Retired entries keep their file with `status: retired` but leave the index.
