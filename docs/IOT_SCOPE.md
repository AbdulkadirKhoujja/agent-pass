# AgentPass scope: services, machines and agentic IoT

AgentPass began as a proposed permission and verification layer for AI agents interacting safely with **services, software tools, machines and connected devices**. This document keeps that original ambition visible without representing it as a shipped capability.

## Trust boundary

An agent proposing an operation is **not** evidence that a person authorized it. A device advertising capabilities is **not** evidence that its claimed identity is genuine. Receipts written by the requester are **not** independently verified execution evidence.

## Proposed interactions

- Read a non-sensitive device's published capability catalogue in a controlled simulation.
- Request a narrowly scoped, time-limited grant from a separately authenticated controller.
- Refuse actions beyond approved scope, destination, risk limit or physical safety preconditions.
- Execute on a dedicated mock endpoint first; record verified observed state, not just a model's claim.
- Return a signed, privacy-conscious audit record only after validating identity, delegation and result.

## Non-negotiable safety

No real locks, motors, energy systems, health equipment, vehicles, industrial controls, financial accounts or personal environments will be operated by the demo. Before any physical pilot: explicit owner/operator permission, safe simulation, independent human emergency stop, local safety controller, rate limits, immutable event evidence, segmentation, replay protection and risk review.

## Next test

Build a disconnected virtual device (capabilities: `read:temperature`; no writes), explicit mocked authority with signed test grants, negative test cases for a wrong device or expired grant, and independent expected/actual state comparison. All tests must remain synthetic until design and security reviews are complete.

See [ROADMAP.md](ROADMAP.md) and [BRING_YOUR_AGENT.md](BRING_YOUR_AGENT.md).
