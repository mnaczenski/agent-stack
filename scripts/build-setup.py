#!/usr/bin/env python3
"""Regenerates plugins/agent-stack/commands/setup.md from plugins/agent-stack/templates/.
Run after changing any template, then commit both."""
import os, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "plugins" / "agent-stack"
T = P / "templates"
files = sorted((str(f.relative_to(T)), f.read_text()) for f in T.rglob("*.md"))
out = ["---", "description: Scaffolds the agent-stack folders and templates into the current repository.", "---",
       "Set up this repository for agent-stack.", "",
       "1. For each file below: if it already exists, skip it and report it. Otherwise create it with exactly the given content.",
       "2. Also create the empty folders knowledge/learnings/ and knowledge/decisions/ (with a .gitkeep each).",
       "3. If no CLAUDE.md exists, do not invent one. Tell the user that /onboard will draft it.",
       "4. Report what was created, then suggest: /onboard for an existing codebase, /pm <idea> for a new feature.",
       "5. Do not commit. The user decides.", ""]
for rel, content in files:
    out += [f"### File: {rel}", "````markdown", content.rstrip("\n"), "````", ""]
(P / "commands" / "setup.md").write_text("\n".join(out))
print(f"setup.md regenerated with {len(files)} templates")
