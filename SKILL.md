---
name: pstack-universal
description: Universal entry point for Pstack across AI harnesses. Applies the canonical Pstack rules without remixing or weakening them, then routes non-trivial work to the repository's Pstack skills.
---

# Pstack Universal

Use this file as the importable root skill for AI systems that expect a repository-level `SKILL.md`.

## Canonical source rule

`PSTACK_GLOBAL.md` is the canonical source of truth.

When that file is accessible, use it directly. Do not replace it with a summary, remix, paraphrase, generated compatibility layer, or platform-specific rewrite.

Platform-specific instructions may add routing or tool mappings only. They may not weaken, omit, or contradict the canonical rules.

If a platform cannot fully apply a canonical rule because of higher-priority system, safety, legal, security, or technical constraints, keep the rule unchanged and report the limitation explicitly.

If `PSTACK_GLOBAL.md` was not actually read, do not claim that full Pstack is loaded or active.

## Start

1. Read `PSTACK_GLOBAL.md` in full.
2. Perform its integrity self-check.
3. For non-trivial engineering or agent work, read `skills/poteto-mode/SKILL.md`.
4. Follow any task-specific Pstack skill that `poteto-mode` routes to.
5. If a referenced file cannot be accessed in the current harness, apply `PSTACK_GLOBAL.md` as the fallback and state that the unavailable nested skill was not loaded.

## Non-negotiable

Never claim that a tool call, verification, test, search, file edit, deployment, message, or other external action happened unless there is direct evidence from the current session.

Never turn an inference into a verified fact.

Never report `PSTACK STATUS: PASS` unless the canonical `PSTACK_GLOBAL.md` was actually read and the integrity self-check passed.

The platform's higher-priority system, safety, and security instructions always remain in force.
