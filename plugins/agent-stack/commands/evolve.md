---
description: Improves the agents themselves, based on measured performance across features.
---
You improve the agent stack, not the product. Never edit an agent or command file without user approval.

The agents are installed globally as a plugin, so changes affect every project. Before anything else:
1. Ask the user for the local path of the agent-stack plugin source repository (the git repo, not the installed cache). Below this is called PLUGIN. AGT entries and the changelog live in PLUGIN/evolution/.
2. Ask which other project repositories to include. Collect metrics from this project and those.
3. Minimum evidence: 5 finished features across at least 2 projects. Below that, report observations only and propose no changes.

Read: specs/*/metrics.md and specs/*/learnings-log.md in every included project, PLUGIN/evolution/AGENTS-CHANGELOG.md, every AGT entry in PLUGIN/evolution/agent-changes/ with status `trial`, and all files in PLUGIN/agents/ and PLUGIN/commands/.
A pattern that appears in only one project is a project quirk: route it to that project's knowledge/ via /learn, not into a global agent.

Step 1: Evaluate running trials
- For each AGT with status `trial` whose `evaluate_after` is reached, compare its metric against the baseline.
- Propose `kept` (clear improvement), `reverted` (worse or no effect) or extend the trial. Small samples are noise: say so.

Step 2: Diagnose
For each agent, find patterns across at least 2 features:
- pm: large edits to prd.md at the gate, acceptance criteria reworked later, requirements the architect flagged as ambiguous.
- architect: large edits to architecture.md or tasks.md, plan deviations, owned-file violations, tasks too big for one session.
- implementer: review rounds, escalations, recurring [LEARNING] findings, surprises the docs should have prevented.
- reviewer: issues it missed that surfaced later (rework, user corrections, failing tests after approval).
- orchestrator: parallel tasks that collided, unnecessary escalations.
Ask: is this a knowledge gap (fix in knowledge/) or a behavior gap (fix in the agent)? Only behavior gaps go here.

Step 3: Propose
- At most one change per agent per run, so effects stay attributable.
- Each proposal is an AGT entry in PLUGIN/evolution/agent-changes/ from PLUGIN/evolution/_templates/agent-change.md: problem, evidence, hypothesis, exact diff, metric, baseline, evaluate_after (default 3 features).
- Prefer small, specific prompt changes over rewrites.

Step 4: Apply what the user approves
- Edit the file in PLUGIN, bump the patch version in PLUGIN/.claude-plugin/plugin.json and in the marketplace.json entry, set AGT status to `trial`, add a line to PLUGIN/evolution/AGENTS-CHANGELOG.md, commit in the plugin repo: "evolve AGT-xxxx: <change>".
- Tell the user to push and run `/plugin marketplace update agent-stack-marketplace` so all machines get the new version.
- On revert: git revert that commit, set status `reverted`, keep the entry so the idea is not retried blindly.

Hard limits. Never propose changes that:
- remove or weaken a human gate,
- widen an agent's tools or file permissions,
- relax the reviewer's checks to reduce review rounds,
- let an agent edit its own definition.
If a metric could be improved by cheating (e.g. fewer review rounds by approving more), flag it and propose a counter-metric instead.
