# Manus AI + Pstack

Preferred entry point: import this repository as a Skill using the root `SKILL.md`.

The root skill points Manus to `PSTACK_GLOBAL.md` and then to `skills/poteto-mode/SKILL.md` for non-trivial work.

If a Manus workspace cannot traverse nested repository files, copy or attach `PSTACK_GLOBAL.md` to that workspace as the fallback. Do not duplicate the rules manually in several places because that creates drift.

Recommended validation prompt after setup:

"State which Pstack files you loaded for this task. Separate verified facts from inference. Do not claim any tool action that you did not actually perform."

Pstack does not override Manus platform safety or system rules.
