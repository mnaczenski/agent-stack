# agent-stack

Spec-driven agent workflow for Claude Code: PM -> Architect -> Build, with codebase onboarding, project memory and agent self-improvement.

## What lives where
| Layer | What | Where |
|---|---|---|
| Behavior | Agents and commands | This plugin, installed once per machine |
| Evolution | Agent changes (AGT), changelog | This repo, plugins/agent-stack/evolution/ |
| Memory | Specs, metrics, learnings, decisions, system map | Each project repo, created by /setup |

Behavior is global and versioned. Memory is per project and lives in that project's git history.

## Install (once per machine)
Push this repo to your git host, then in Claude Code:
```
/plugin marketplace add <org>/agent-stack-marketplace
/plugin install agent-stack@agent-stack-marketplace
```
For local testing: `/plugin marketplace add ./agent-stack-marketplace`.
Plugin commands may also appear namespaced, e.g. `/agent-stack:pm`.

For a team: add the marketplace to the project's `.claude/settings.json` so everyone is prompted to install it.

## Use in a project
0. `/setup`  Once per repo. Scaffolds specs/, knowledge/, docs/system/ with templates
1. `/onboard`  Existing codebases. System map, capabilities, CLAUDE.md draft
2. `/pm <idea>`  Interview, PRD. Gate: you approve
3. `/plan <slug>`  Architecture and tasks. Gate: you approve
4. `/build <slug>`  Implement, review, commit per task, record metrics
5. `/retro <slug>`  Turn observations into learnings and decisions. Gate: you approve

Anytime: `/learn <rule>`, monthly: `/tidy`.
Every 5+ features across 2+ projects: `/evolve` improves the agents in this plugin.

## Two loops
- Knowledge loop (/retro, per project): what agents know about a codebase.
- Behavior loop (/evolve, cross-project): how agents work. One change per agent, trialled, kept or reverted on evidence. Project quirks go to that project's knowledge, never into global agents.

## Updating
- Agents or commands: edit, bump version in plugin.json and marketplace.json, push. Users run `/plugin marketplace update agent-stack-marketplace`.
- Templates: edit plugins/agent-stack/templates/, then run `python3 scripts/build-setup.py` to regenerate /setup. Existing projects keep their copies; new templates only reach new setups.

## Principles
- Artifacts in the repo are the interface between agents, not chat context.
- Humans approve WHY/WHAT, the plan, new memory and agent changes.
- Parallel tasks never share files.
- Memory is retrieved by index, not loaded wholesale. CLAUDE.md stays small.
- Agents never edit their own definitions and never weaken gates, tools or checks.
- Code tells you WHAT. Only people tell you WHY. Inferred intent is always marked.
