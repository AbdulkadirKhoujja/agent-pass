# Product roadmap

**Phase 0 — public foundation (in progress)**

- [x] Public repo, README, license, security/contribution guidelines.
- [x] Offline, deterministic discovery/permission/action/receipt demonstration.
- [x] Positive and negative tests for supported synthetic scenarios.
- [x] CI test workflow and first-party discoverability content (subject to CI/Page activation).
- [ ] Obtain GitHub CI pass on the published commit and independently verify Pages is publicly reachable.

**Phase 1 — rigorous contracts**

- [ ] Machine-readable draft JSON schemas and strict input validation.
- [ ] Threat model and security invariants / failure-mode suite.
- [ ] Signed receipts, verification, replay defense, clock/audience checks.
- [ ] Persisted audit tests and privacy/data minimization requirements.
- [ ] External reviewer and reproducible fixtures.

**Phase 2 — real-world consent and authorization**

- [ ] OAuth/OIDC integration where appropriate; do not build identity proofs from untrusted fields.
- [ ] End-user consent + explicit delegation, scoped permissions, revocation and expiry.
- [ ] AuthZEN mapping / actual PDP + PEP enforcement with interop tests.
- [ ] Security tests and gated staging evaluation without real client data.

**Phase 3 — genuine integrations**

- [ ] A2A Agent Card and server only after implementing compatible A2A endpoints.
- [ ] MCP server and official registry submission only when actually runnable.
- [ ] Well-defined SDKs and integration examples with contract and negative tests.
- [ ] Partner pilot with opt-in and consent.

**Phase 4 — safe public adoption**

- [ ] Independent security review and verified implementation claims.
- [ ] Public benchmark report with exact methodology, failures and reproducible runs.
- [ ] Maintainer-approved upstream contributions; no promotional issue spam.
- [ ] Measured discovery → docs → install → successful test → repeat usage funnel.

Roadmap checkboxes are planning status, **not** proof of readiness.
