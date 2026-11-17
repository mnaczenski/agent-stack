---
description: Scaffolds the agent-stack folders and templates into the current repository.
---
Set up this repository for agent-stack.

1. For each file below: if it already exists, skip it and report it. Otherwise create it with exactly the given content.
2. Also create the empty folders knowledge/learnings/ and knowledge/decisions/ (with a .gitkeep each).
3. If no CLAUDE.md exists, do not invent one. Tell the user that /onboard will draft it.
4. Report what was created, then suggest: /onboard for an existing codebase, /pm <idea> for a new feature.
5. Do not commit. The user decides.

### File: docs/system/_templates/capabilities.md
````markdown
# Capabilities (as built)
What the product does today, from a user's perspective. This is the baseline new PRDs build on.

| Capability | Users | Modules | Status | Why (if known) |
|---|---|---|---|---|

## Open questions about intent
````

### File: docs/system/_templates/module.md
````markdown
# Module: <name>
_Path: <path>_

## Responsibility

## Entry points and interfaces

## Data model

## Dependencies
- Uses:
- Used by:

## Patterns and conventions

## Tests

## Hotspots

## Risks

## Open questions
````

### File: docs/system/_templates/overview.md
````markdown
# System overview
_Last updated: <date> by /onboard_

## What the system is

## Tech stack

## Modules
| Module | Responsibility | Doc |
|---|---|---|

## How modules interact

## Cross-cutting concerns (auth, config, i18n, caching, events)

## Global hotspots

## Open questions
````

### File: knowledge/INDEX.md
````markdown
# Knowledge index
One line per entry. Agents read this file first, then open only the entries relevant to their module or task.
Maintained by /learn, /retro and /tidy. Keep it short: retired entries are removed from this index.

## Learnings
| ID | Type | Scope | Summary | Status |
|---|---|---|---|---|

## Decisions
| ID | Title | Scope | Status |
|---|---|---|---|
````

### File: knowledge/_templates/decision.md
````markdown
---
id: ADR-0000
status: proposed | accepted | superseded by ADR-xxxx
scope: global | <module>
created: <date>
source: <FEAT id>
---
# <Decision title>

## Context

## Decision

## Alternatives considered

## Consequences
````

### File: knowledge/_templates/learning.md
````markdown
---
id: LRN-0000
type: mistake | convention | gotcha | preference
scope: global | <module>
status: proposed | accepted | retired
created: <date>
source: <FEAT id, task, PR, or "user">
seen: 1
---
# <One-line rule, phrased as an instruction>

## Context
What happened, with file paths.

## Rule
What agents must do differently. Concrete and checkable.

## Example
Wrong:
Right:
````

### File: specs/INDEX.md
````markdown
# Feature board
One line per feature. Updated by /pm, /plan and /build.

| ID | Slug | Title | Status | Created | Done | Outcome |
|---|---|---|---|---|---|---|
````

### File: specs/_templates/architecture.md
````markdown
---
status: draft
prd: ./prd.md
---
# Architecture: <Title>

## Approach summary

## Current state (relevant code with paths)

## Proposed design

## Data model and migrations

## APIs and interfaces

## Alternatives considered
Mark choices worth recording as an ADR with [ADR candidate].

## Risks and mitigations

## Test strategy

## Requirement traceability
| Requirement | Components | Tasks |
|---|---|---|

## Open questions
````

### File: specs/_templates/learnings-log.md
````markdown
# Learning candidates: <FEAT id>
Raw log written during /build. Reviewed by /retro. Not read by other features.

| When | Task | Source | Observation |
|---|---|---|---|
````

### File: specs/_templates/metrics.md
````markdown
# Run metrics: <FEAT id>
Written during the flow. Read by /retro and /evolve.

## Gate edits (how much the human changed agent drafts)
| Artifact | Lines changed | Sections changed | Main reason |
|---|---|---|---|
| prd.md | | | |
| architecture.md | | | |
| tasks.md | | | |

## Build
| Task | Review rounds | Escalated | Plan deviation | Owned-file violation |
|---|---|---|---|---|

## Outcome
- Acceptance criteria met first time:
- Acceptance criteria needing rework:
- Total escalations to user:
- agent-stack plugin version:
````

### File: specs/_templates/prd.md
````markdown
---
id: FEAT-0000
status: draft
owner:
created:
related: []
---
# <Title>

## Problem (WHY)
What problem, for whom, and what evidence do we have? What happens if we do nothing?

## Target users and context

## Goals and success metrics

## Non-goals

## Requirements (WHAT)
- R1:
- R2:

## Acceptance criteria
- R1: Given ... When ... Then ...

## Constraints and dependencies

## Open questions

## Decision log
````

### File: specs/_templates/tasks.md
````markdown
# Tasks: <Title>

| ID | Title | Depends on | Requirements | Status |
|---|---|---|---|---|
| T1 | | | | todo |

## T1: <Title>
- Goal:
- Owns files:
- Depends on:
- Requirements:
- Done when:
````
