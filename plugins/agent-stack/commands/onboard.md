---
description: Reverse engineers an existing repository into a system map, conventions and as-built capabilities.
argument-hint: [optional: path or area to focus on]
---
You are onboarding this agent stack onto an existing codebase. Focus: $ARGUMENTS (if empty, the whole repository).

Goal: a baseline in docs/system/ that future /pm, /plan and /build runs read instead of re-exploring the code.

If specs/_templates/ does not exist, run the /setup steps first (create the scaffold), then continue.

Phase 1: Survey (you, quickly)
- Read README, existing docs, package manifests, CI config, Dockerfiles, top-level directory structure.
- Identify the main modules or bounded contexts. Propose a list of 3 to 10 modules to the user and ask for confirmation before continuing.

Phase 2: Map (parallel)
- For each confirmed module, delegate to the `cartographer` subagent with the module name and path. Modules can run in parallel.

Phase 3: Synthesize (you)
- Write docs/system/overview.md from docs/system/_templates/overview.md, based on the module docs.
- Write docs/system/capabilities.md from docs/system/_templates/capabilities.md: what the product does today, from a user's perspective.
- Seed knowledge/ with `status: proposed` decisions for architectural choices clearly visible in the code (framework, data access, eventing, extension model). Ask the user to confirm them.
- Draft CLAUDE.md (or propose changes if one exists): build, test, lint and run commands you verified actually work, plus conventions observed in the code.

Rules:
- Mark every statement as `[verified]` (seen in code, tests or by running a command) or `[inferred]` (your interpretation).
- The WHY behind existing features is rarely in the code. Never invent it. Put it under "Open questions" and list the people or sources that could answer it.
- Do not modify any source code.

Finish with: what was mapped, what could not be verified, and the 5 most important open questions for the user.
