---
name: pstack-universal
description: Universal entry point for Pstack across AI harnesses. Applies the canonical Pstack rules without remixing or weakening them, verifies the canonical version/checksum, then routes non-trivial work to the repository's Pstack skills.
---

# Pstack Universal

Use this file as the importable root skill for AI systems that expect a repository-level `SKILL.md`.

## Canonical source rule

`PSTACK_GLOBAL.md` is the canonical source of truth.

When that file is accessible, use it directly. Do not replace it with a summary, remix, paraphrase, generated compatibility layer, or platform-specific rewrite.

Platform-specific instructions may add routing or tool mappings only. They may not weaken, omit, or contradict the canonical rules.

If a platform cannot fully apply a canonical rule because of higher-priority system, safety, legal, security, or technical constraints, keep the rule unchanged and report the limitation explicitly.

If `PSTACK_GLOBAL.md` was not actually read, do not claim that full Pstack is loaded or active.

## Version and checksum gate

Before reporting `PSTACK STATUS: PASS`:

1. Read `PSTACK_VERSION`.
2. Read `PSTACK_MANIFEST.json`.
3. Read the current `PSTACK_GLOBAL.md` directly.
4. Verify the Git blob SHA-1 of `PSTACK_GLOBAL.md` against `canonical_git_blob_sha1` in the manifest, either by running `tools/verify_pstack.py` or by an equivalent direct calculation.
5. Report the version, expected checksum, actual checksum, and canonical file name.
6. If checksum verification cannot be performed, report `PSTACK STATUS: PARTIAL`, not PASS.
7. If the canonical file is missing, replaced by a remix, or checksum verification fails, report `PSTACK STATUS: FAIL`.

## Start

1. Complete the version and checksum gate.
2. Perform the integrity self-check in `PSTACK_GLOBAL.md`.
3. For non-trivial engineering or agent work, read `skills/poteto-mode/SKILL.md`.
4. Follow any task-specific Pstack skill that `poteto-mode` routes to.
5. If a referenced file cannot be accessed in the current harness, apply `PSTACK_GLOBAL.md` as the fallback and state that the unavailable nested skill was not loaded.

## Non-negotiable

Never claim that a tool call, verification, test, search, file edit, deployment, message, or other external action happened unless there is direct evidence from the current session.

Never turn an inference into a verified fact.

Never report `PSTACK STATUS: PASS` unless the canonical `PSTACK_GLOBAL.md` was actually read, the checksum matched `PSTACK_MANIFEST.json`, and the integrity self-check passed.

The platform's higher-priority system, safety, and security instructions always remain in force.
