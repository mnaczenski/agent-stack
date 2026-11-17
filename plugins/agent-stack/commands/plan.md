---
description: Architect plans architecture and tasks for an approved PRD.
argument-hint: <slug>
---
If specs/_templates/ does not exist in this repository, stop and tell the user to run /setup first.

Read specs/$ARGUMENTS/prd.md. If its status is not `approved`, stop and tell the user.

Compare specs/$ARGUMENTS/.drafts/prd.md with prd.md (git diff --no-index --stat plus a read of both). Record lines and sections changed and the main reason in metrics.md under Gate edits.

Delegate to the `architect` subagent with the slug $ARGUMENTS.

When it returns, save identical copies of architecture.md and tasks.md to specs/$ARGUMENTS/.drafts/.

When it returns, show the user:
1. The approach in 3 to 5 sentences
2. The top 3 risks
3. The task graph: which tasks run in parallel, which are sequential

Ask the user to review specs/$ARGUMENTS/architecture.md and tasks.md, set `status: approved` in architecture.md, then run /build $ARGUMENTS. Set the feature status in specs/INDEX.md to `planned`. Do not start implementation.
