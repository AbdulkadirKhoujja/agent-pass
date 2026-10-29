# Ecosystem contribution queue (30% track)

The objective is to be **useful upstream**, not to plant AgentPass advertisements.

## Target 1: OpenID AuthZEN

Reference: https://openid.net/wg/authzen/specifications/ — Authorization API 1.0 became a final specification in January 2026.

**Candidate contribution:** find and reproduce a real ambiguity or missing edge-case test in authorization decision request/response handling. Establish test coverage in a separate harness; only propose a PR after confirming current upstream guidance and contribution conventions.

**Current status:** research target only, no upstream PR submitted and no compatibility claimed.

## Target 2: A2A

Reference: https://a2a-protocol.org/latest/topics/agent-discovery/

**Candidate contribution:** improve safe and accessible Agent Card discovery guidance or add a negative test around missing/unsafe metadata. Do **not** publish `/.well-known/agent-card.json` for AgentPass until a real A2A server and correct card exist.

**Current status:** research target only.

## Target 3: MCP

Reference: https://modelcontextprotocol.io/ and https://registry.modelcontextprotocol.io/docs

**Candidate contribution:** reproducible server configuration, schema validation or security documentation, tied to an existing maintainers' issue. Do not register a fake or unreachable MCP server to gain exposure.

**Current status:** research target only.

## Review process

1. Select a currently open upstream issue and read maintainer guidelines.
2. Produce a minimal, independent reproducer or documentation fix with no AgentPass dependency.
3. Verify behavior against the current upstream specification and tests.
4. Ask for feedback where appropriate; do not auto-submit mass PRs or use promotional comments.
5. Report outcome precisely: proposed / opened / under review / merged / rejected; never call “drafted” merged.
6. Keep a log with source issue URL, test instructions, last checked date, review feedback and disclosure of conflicts.

No production credentials, proprietary code, confidential client data, or automated outreach belongs in this contribution programme.
