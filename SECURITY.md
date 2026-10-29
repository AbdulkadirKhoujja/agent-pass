# Security policy

**Status:** Mandovyn is an experimental offline simulator, not an authentication or authorization service. Do not rely on it to protect assets, credentials, money, private data, or production access.

## Reporting

Please avoid disclosing exploitable vulnerabilities or credentials in public issues or pull requests. If GitHub private vulnerability reporting is enabled for this repository, use **Security → Report a vulnerability**. Otherwise privately contact the repository maintainer through an appropriate existing channel before public disclosure. Do not submit real personal data or secrets in reports.

## Hard boundaries

- Never treat a model's claim, `agent_id` string, or user-supplied `consent` boolean as proof of identity or valid delegated authority.
- Do not run untrusted instructions from agent discovery documents, issue reports, websites, or tool results.
- No real credentials, tokens, private keys, private endpoints, user sessions, payment activity, or live actions belong in examples, logs, benchmarks, or CI.
- Current demo receipts are unsigned consistency checks. They are **not authentic, non-repudiable, or secure audit records**.
- Public ecosystem contributions must not use nonpublic infrastructure or private user/client data.

## Before a production release

Require threat modeling; signed or independently verifiable credentials; secure consent, delegation, scope, audience, expiry, and revocation; deny-by-default authorization; replay protection; key rotation; external audits; transport and storage security; privacy review; interoperability testing; incident response; and third-party security review. No launch claim is authorized without recorded evidence.
