---
description: Orchestrates implementation of an approved plan.
argument-hint: <slug>
---
If specs/_templates/ does not exist in this repository, stop and tell the user to run /setup first.

Read specs/$ARGUMENTS/prd.md, architecture.md and tasks.md. If architecture.md status is not `approved`, stop and tell the user.

You are the orchestrator. You do not write code yourself.
Compare the drafts in specs/$ARGUMENTS/.drafts/ with the approved architecture.md and tasks.md and record the gate edits in metrics.md. Record the agent-stack plugin version (from the installed plugin, or ask the user) in metrics.md.
Set the feature status in specs/INDEX.md to `in-progress`. Create specs/$ARGUMENTS/learnings-log.md from specs/_templates/learnings-log.md.

Loop until all tasks are done:
1. Select all tasks with status `todo` whose dependencies are `done`.
2. Delegate each selected task to the `implementer` subagent (slug + task ID). Tasks with no overlapping owned files may run in parallel.
3. When an implementer returns, delegate the same task to the `reviewer` subagent.
4. If the reviewer returns CHANGES_REQUESTED, pass the findings back to the implementer. After 2 failed rounds, stop and escalate to the user.
   Log every [LEARNING] finding, every second review round, and every implementer surprise in learnings-log.md.
   Record per task in metrics.md: review rounds, escalation, plan deviation, owned-file violation.
5. If APPROVED, set the task status to `done` in tasks.md and commit: "$ARGUMENTS T<n>: <title>".

When finished, run the full test suite and report to the user, mapped to each PRD acceptance criterion: met, partially met, not met.
Update docs/system/ for the modules that changed and add the new capability to capabilities.md.
Fill in the Outcome section of metrics.md.
Set the feature status in specs/INDEX.md to `done`. Then tell the user to run /retro $ARGUMENTS. Do not write to knowledge/ yourself.
