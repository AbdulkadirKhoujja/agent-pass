# Mandovyn protocol sketch (NOT a specification)

This document describes a possible future protocol, not a deployed standard or a production API.

## Proposed lifecycle

1. **Discover**: a relying party or agent finds a trustworthy, authenticated service descriptor.
2. **Understand**: read supported action verbs, resources, permission requirements, and privacy policy.
3. **Obtain authority**: authenticate real actors and obtain explicit, appropriately scoped permission.
4. **Authorize**: deny by default; evaluate principal, action, resource, context, time, audience, and revocation.
5. **Execute**: perform the approved action exactly once, with independent policy enforcement.
6. **Verify**: verify the actual observed result against the grant and expected operation.
7. **Receipt**: produce a minimal signed/verifiable record with redaction, retention, and dispute handling.

## Current, implemented simulator

Run `python -m mandovyn --describe`, then `python -m mandovyn examples/allowed_request.json`.

The following input is **not a real permission grant**:

```json
{
  "agent_id": "example-agent-unverified",
  "action": "demo:read",
  "resource": "demo:catalog",
  "consent": true
}
```

The simulator accepts only `demo:read` on `demo:catalog`, with a caller-supplied test consent flag, and returns `["alpha", "beta"]` plus a checksum-only receipt. All data and results are synthetic; there are no external effects.

## Questions to settle before a protocol

- What independently attests an agent, its controller, and the human or organization represented?
- What is the representation of constrained delegations, expiry, revocation and audience?
- Which actor is liable for actions and what is a trustworthy execution record?
- How does revocation propagate to concurrent tasks and offline agents?
- How do we interoperate with OAuth/OIDC, OpenID AuthZEN, A2A, and MCP without inventing incompatible semantics?
- How do we minimize disclosure, preserve consent, and protect against replay, tampering, prompt injection and confused-deputy attacks?

## Compatibility claims

**None.** A2A Agent Cards are published by actual A2A servers at `/.well-known/agent-card.json`; an HTML site or JSON sketch is not an Agent Card. A live MCP server, package metadata and conformance testing are prerequisites to MCP registry publication. AuthZEN's final Authorization API is the interoperability reference for authorization decisions. We will publish compatibility artifacts only when each corresponding interface is really implemented and tested.

References: [OpenID AuthZEN](https://openid.net/wg/authzen/specifications/) · [A2A](https://a2a-protocol.org/) · [MCP](https://modelcontextprotocol.io/).
