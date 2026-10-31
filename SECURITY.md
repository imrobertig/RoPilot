# Security notes

RoPilot can eventually modify a Roblox project, so its local bridge must be treated as a privileged interface.

1. Bind only to `127.0.0.1` unless a deliberate, authenticated remote mode is implemented.
2. Store provider secrets in local environment/config storage, never in extension source.
3. Never execute arbitrary shell commands supplied by a model.
4. Use a strict tool allowlist with typed input validation.
5. Show diffs before applying script rewrites.
6. Require explicit confirmation for deletion, large-scale edits, publishing, and other irreversible actions.
7. Add request IDs, timeouts, output limits, and cancellation.
8. Do not collect Roblox cookies, passwords, or browser session tokens.
