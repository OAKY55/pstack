# Manus AI + Pstack

Preferred entry point: import this repository as a Skill using the root `SKILL.md`.

The root skill points Manus to `PSTACK_GLOBAL.md` and then to `skills/poteto-mode/SKILL.md` for non-trivial work.

## Canonical rule

Manus should use the current `PSTACK_GLOBAL.md` directly when it is accessible.

A Manus-generated remix, compatible rewrite, summary, shortened copy, or replacement skill is not the canonical Pstack rules and must not be treated as equivalent to the original file.

Manus-specific instructions may add routing or tool mappings, but they should not weaken, omit, contradict, or replace the canonical rules.

## Required version and checksum check

Before Manus reports `PSTACK STATUS: PASS`, it must:

1. read `PSTACK_VERSION`;
2. read `PSTACK_MANIFEST.json`;
3. read the current `PSTACK_GLOBAL.md` directly;
4. verify the Git blob SHA-1 of `PSTACK_GLOBAL.md` against `canonical_git_blob_sha1`;
5. report the version, canonical filename, expected checksum, and actual checksum.

If Manus cannot perform the checksum verification, it must report `PSTACK STATUS: PARTIAL`.

If Manus only loaded a generated remix or summary, or the checksum does not match, it must report `PSTACK STATUS: FAIL`.

If a Manus workspace cannot traverse nested repository files, copy or attach `PSTACK_GLOBAL.md`, `PSTACK_VERSION`, and `PSTACK_MANIFEST.json` to that workspace as the fallback. Do not duplicate the rules manually in several places because that creates drift.

Recommended validation prompt after setup:

"Report PSTACK_VERSION, the canonical file name, the expected checksum from PSTACK_MANIFEST.json, and the actual checksum you verified. State exactly which files you read directly. Confirm whether you read the current PSTACK_GLOBAL.md directly or only a generated remix. Return PSTACK STATUS: PASS, PARTIAL, or FAIL. Never return PASS if the canonical checksum was not verified."

Pstack does not override Manus platform safety or system rules.
