# Manus AI + Pstack

Preferred entry point: import this repository as a Skill using the root `SKILL.md`.

The root skill points Manus to `PSTACK_GLOBAL.md` and then to `skills/poteto-mode/SKILL.md` for non-trivial work.

## Canonical rule

Manus should use the current `PSTACK_GLOBAL.md` directly when it is accessible.

A Manus-generated remix, compatible rewrite, summary, shortened copy, or replacement skill is not the canonical Pstack rules and must not be treated as equivalent to the original file.

Manus-specific instructions may add routing or tool mappings, but they should not weaken, omit, contradict, or replace the canonical rules.

If Manus cannot access the canonical file or a nested skill, report the limitation explicitly. Do not report `PSTACK STATUS: PASS` unless the current canonical `PSTACK_GLOBAL.md` was actually read and the integrity self-check passed.

If a Manus workspace cannot traverse nested repository files, copy or attach `PSTACK_GLOBAL.md` to that workspace as the fallback. Do not duplicate the rules manually in several places because that creates drift.

Recommended validation prompt after setup:

"State which Pstack files you loaded for this task. Confirm whether you read the current PSTACK_GLOBAL.md directly or only a generated remix. Separate verified facts from inference. Do not claim any tool action that you did not actually perform. Return PSTACK STATUS: PASS, PARTIAL, or FAIL."

Pstack does not override Manus platform safety or system rules.
