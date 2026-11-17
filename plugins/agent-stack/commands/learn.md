---
description: Capture a learning or decision manually.
argument-hint: <what should be remembered>
---
If specs/_templates/ does not exist in this repository, stop and tell the user to run /setup first.

The user wants this remembered: $ARGUMENTS

1. Read knowledge/INDEX.md. If an existing entry covers it, update that entry (increase `seen`, sharpen the rule) instead of creating a new one.
2. Decide the kind: a learning (how to work in this codebase) or a decision (an architectural choice with alternatives). Ask the user if unclear.
3. Create the entry from knowledge/_templates/, next free ID, `status: accepted` (the user stated it directly).
4. Phrase the rule as a concrete instruction an agent can follow and a reviewer can check.
5. Add one line to knowledge/INDEX.md.
