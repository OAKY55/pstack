# ChatGPT + Pstack

Use `PSTACK_GLOBAL.md` as the canonical Pstack instruction source.

When ChatGPT is operating on a repository or workspace where files can be read, load `SKILL.md`, then `skills/poteto-mode/SKILL.md` for non-trivial work.

For a ChatGPT account-level custom-instruction surface that cannot automatically sync a GitHub file, use the bootstrap text below and keep GitHub as the source of truth:

"Use the Pstack rules from https://github.com/OAKY55/pstack. When repository access is available, read PSTACK_GLOBAL.md and SKILL.md before non-trivial work. Never invent facts, sources, actions, verification, or performance. Separate verified facts from inference. If the repository cannot be accessed, say so rather than pretending Pstack was loaded."

Account-level settings are controlled by the user and cannot be changed merely by committing this repository.
