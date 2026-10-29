# Mandovyn

**A public, experimental foundation for AI-agent discovery, delegated permissions, action verification, and receipts.**

[![CI](https://github.com/AbdulkadirKhoujja/mandovyn/actions/workflows/ci.yml/badge.svg)](https://github.com/AbdulkadirKhoujja/mandovyn/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

> **Status: early proof of concept, not a production authentication, identity, authorization, or payment service.** The bundled simulator uses fictitious agents and local policy checks; it does **not** verify actual identities or execute real-world actions. No A2A, MCP, or AuthZEN compliance is claimed.

## The idea

AI agents need predictable ways to discover what they may do, request user-granted authority, act within those boundaries, and explain what happened. Mandovyn explores a simple, auditable journey:

`Discover → Understand → Request authority → Check permission → Simulate action → Verify → Produce receipt`

The initial demo is intentionally offline and dependency-free. Real identity validation, delegated authorization, interoperable transports, and cryptographically verifiable receipts are **future research and implementation milestones**, not existing features.

## Run the local demo

Requires Python 3.10 or newer. No third-party dependencies.

```sh
python -m mandovyn
python -m mandovyn examples/allowed_request.json
python -m unittest discover -s tests -v
```

An allowed request produces a synthetic catalogue result and a **checksum-only** demo receipt. A denied request produces an explicit explanation and **no action**. The receipt checksum detects incidental modification within the demo, but does **not** provide authenticity or tamper resistance against an attacker.

## Start here

- [Protocol sketch](docs/PROTOCOL_DRAFT.md)
- [Development roadmap](docs/ROADMAP.md)
- [Distribution and discoverability strategy](docs/DISTRIBUTION.md)
- [Ecosystem contributions plan](docs/ECOSYSTEM_CONTRIBUTIONS.md)
- [Benchmark methodology](docs/BENCHMARKS.md)
- [Security boundaries](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [Project landing page source](docs/index.html)

## Distribution thesis

**70% product, 30% ecosystem.** Build useful, documented software, then contribute independently valuable upstream work to [OpenID AuthZEN](https://openid.net/wg/authzen/specifications/), [A2A](https://a2a-protocol.org/), and [Model Context Protocol](https://modelcontextprotocol.io/) where maintainers welcome it. Seek interoperability, not implied endorsement.

The repository includes a search-readable landing page and `llms.txt`. Discoverability does not make this implementation an official MCP server or A2A agent. Registry entries and protocol conformance will follow only after actual compatible endpoints exist.

## Physical-world and machine interactions (research direction)

Mandovyn's longer-term scope includes **permissioned agent interactions with services, machines and IoT devices**. All connected-device access, capability discovery, device/user attestation, safety interlocks, and audit records remain future work. This repository's demo does not contact any device.

- [Bring Your Agent evaluation plan](docs/BRING_YOUR_AGENT.md)
- [Machine and IoT boundary plan](docs/IOT_SCOPE.md)

## Naming and independence

Mandovyn was previously developed under the working name **AgentPass**. We changed it to distinguish this independent project from an unrelated product. See [naming history](docs/NAMING.md). This project does not claim affiliation with Clerk or any standards organization.

## Trust and openness

Do not store credentials, private user workflows, identity documents, secrets, production receipts, or real authorization decisions in this repository. Never infer consent from discovery or a model-generated statement. Report vulnerabilities privately, as described in [SECURITY.md](SECURITY.md).

## Domain ownership

The `mandovyn.com` domain was reported available when checked, but is **not registered or owned by this project** at this stage. Use GitHub as the only verified canonical contact point until registration is confirmed.

## License

Apache License 2.0. See [LICENSE](LICENSE).
