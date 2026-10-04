# Qwen + Pstack

Use `PSTACK_GLOBAL.md` as the central Pstack rules.

For Qwen coding/agent environments that can read repository files, load `SKILL.md`, then `skills/poteto-mode/SKILL.md` and any routed skills.

For a personal/global instruction surface that cannot sync the repository automatically, use this bootstrap:

"Use https://github.com/OAKY55/pstack as the source of truth. Read PSTACK_GLOBAL.md and SKILL.md when accessible. Never fabricate facts, sources, tool actions, tests, or verification. Separate verified facts from inference. If repository access is unavailable, state that limitation."

Do not fork the full rule text into a separate copy unless the platform requires it.
