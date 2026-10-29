# Benchmark and evidence policy

## Current baseline

The initial suite covers ten deterministic unit tests around a local, synthetic demo. A passing test demonstrates expected behavior **for only those fixtures**, not cryptographic authenticity, identity assurance, real consent, production security, or interoperability.

Reproduce:

```sh
python -m unittest discover -s tests -v
```

Tests include successful synthetic response, local-policy denials, invalid request handling, and checksum consistency. The checksum is unsigned and can be recomputed by anyone; no third-party verification exists.

## Future benchmark categories

| Category | Positive and negative cases | Not-yet-established evidence |
| --- | --- | --- |
| Discovery | Valid/invalid metadata, cache and trust boundary | Authenticated discovery |
| Identity | Verified agent and controller, spoof/replay failures | Real identity provider proofs |
| Authorization | Consent, scoped grant, deny-by-default, revocation | AuthZEN interoperability |
| Execution | Idempotency, wrong-target denial, response capture | Real controlled endpoints |
| Receipts | Genuine signatures, tamper/replay and key rotation | Independent verifier |
| Privacy | Data minimization and retention, leakage failures | External audit |
| Integrations | A2A/MCP versions, network faults, error handling | Live conformance evidence |
| Adoption | Repeat usage, real integrations, support burden | Observable adoption |

## Reporting rules

Each result must declare version, commit SHA, fixture hash, command, machine/runtime, sample count, failure cases, expected versus observed behavior, and whether it is synthetic or live. Disclose missing fixtures, environment limitations and test bias. Never transform a local unit-test pass into a public certification claim. Separate independent tests from developer self-tests.
