---
name: pstack-universal
description: Universal entry point for Pstack across AI harnesses. Applies evidence-first, verified execution rules and routes non-trivial work to the repository's Pstack skills.
---

# Pstack Universal

Use this file as the importable root skill for AI systems that expect a repository-level `SKILL.md`.

## Start

1. Read `PSTACK_GLOBAL.md`.
2. For non-trivial engineering or agent work, read `skills/poteto-mode/SKILL.md`.
3. Follow any task-specific Pstack skill that `poteto-mode` routes to.
4. If a referenced file cannot be accessed in the current harness, apply `PSTACK_GLOBAL.md` as the fallback and state that the unavailable nested skill was not loaded.

## Non-negotiable

Never claim that a tool call, verification, test, search, file edit, deployment, message, or other external action happened unless there is direct evidence from the current session.

Never turn an inference into a verified fact.

The platform's higher-priority system, safety, and security instructions always remain in force.
