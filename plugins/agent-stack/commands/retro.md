---
description: Turns a finished feature into durable knowledge.
argument-hint: <slug>
---
If specs/_templates/ does not exist in this repository, stop and tell the user to run /setup first.

Run a retrospective for specs/$ARGUMENTS.

Read: prd.md, architecture.md, tasks.md, learnings-log.md, the git log for this feature, and knowledge/INDEX.md.

1. Cluster the observations in learnings-log.md. Ignore one-off noise.
2. For each cluster, check knowledge/INDEX.md:
   - Already covered: increase `seen` on that entry. If an accepted rule was violated anyway, propose making it stricter or moving it to CLAUDE.md.
   - New: draft a learning with `status: proposed`.
3. For each significant design choice in architecture.md that is not yet recorded, draft an ADR with `status: proposed`.
4. Compare the outcome with the PRD: which acceptance criteria needed rework, and why? That is a learning about planning or requirements, not only code.
5. Read metrics.md. For anything that points to how an agent behaved rather than what it knew, do not create a learning. List it as an agent-behavior observation for /evolve.
6. Present all proposals to the user as a short list: accept, edit or reject each.
7. Write accepted entries, update knowledge/INDEX.md, update the `outcome` column in specs/INDEX.md.

Promotion rule: a learning with scope `global` and `seen` >= 3 is proposed for CLAUDE.md. Scoped learnings go into the module doc in docs/system/modules/ instead.
