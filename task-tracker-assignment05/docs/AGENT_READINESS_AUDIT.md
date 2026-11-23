# Agent-Readiness Audit

## Assessment

**Assigned level: 2 — Documented.** The repository has readable module boundaries, setup/test commands, a root `AGENTS.md`, explicit safe/forbidden actions, and a repeatable local test suite. Level 3 (Agent-ready) is not claimed because instructions are not enforced technically and broader CI/security evidence is absent.

| Area | Evidence | Assessment |
|---|---|---|
| Readable structure | `app/` separates model, service, storage, CLI and strategies. | Pass |
| README accuracy | README documents Python 3.10+, commands, standard-library-only runtime. | Pass; commands were exercised in this environment. |
| Reproducible setup | No third-party runtime dependencies. | Pass for local CLI; supported OS matrix not tested. |
| Pinned dependencies | No external runtime dependencies to pin. | Not applicable; Python interpreter version is a stated minimum, not a lockfile. |
| Tests | Standard-library unittest suite. | Pass; see `evidence/final_test_output.txt`. |
| Lint / type checks | No linter or type checker configured. | Not run; no claim of lint/type-clean status. |
| Build | No packaging/build system; `compileall` is used as a syntax/bytecode compilation check. | Pass; not equivalent to a distributable build. |
| Logging | CLI prints concise errors to stderr; no structured logging. | Basic only; acceptable for local educational CLI, not production observability. |
| Security safeguards | No network service, authentication, secrets, or third-party runtime packages. Agent scope is documented. | Limited; local file permissions and untrusted JSON schema hardening are not comprehensive. |
| Agent permissions | `AGENTS.md` defines allowed/forbidden actions and human review. | Documented, not technically enforced. |

## Missing evidence / next steps

- Add CI on supported Python versions.
- Add static linting and type checking if the project grows.
- Test on Windows, macOS and Linux.
- Consider file locking and backup/recovery if concurrent writers or important data are introduced.
- Add schema validation/versioning for externally edited JSON files.
- Use a real sandbox/branch protection policy for agents; `AGENTS.md` alone is not a security boundary.
