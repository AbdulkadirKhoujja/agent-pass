# Bring Your Agent — future interoperability study

**Status: proposal only.** No live AI model has been evaluated by this repository.

## Research goal

Test whether different AI assistant environments can discover an appropriately defined service, understand available actions, obtain real delegated authority, honor permission boundaries, execute permitted operations and correctly report verifiable receipts.

## Planned participants

- OpenAI-based agents
- Claude-based agents
- Gemini-based agents
- Open-source / local agents

No vendor is affiliated with or endorses AgentPass merely by participating in future tests.

## Protocol evaluation dimensions

1. Discovery and capability interpretation
2. Agent/controller authentication (with independent identity evidence)
3. Correct consent and delegation behavior
4. Permission enforcement and refusal of out-of-scope actions
5. Exact action and result attribution
6. Verifiable receipts, replay defenses and privacy protection
7. Resilience to ambiguous instructions, prompt injection, and failed tool calls

## Test environment

Begin with local deterministic fixtures. Proceed to sandboxed tools and mock services only after a clear threat model; real machines, IoT devices or personal accounts require explicit authorization and independent safety measures. Keep controlled targets isolated.

## Public benchmark format

For every agent/runtime: version/date, task fixture identifier, permissions presented, expected result, observed result, refusals, error classes, input/output artifacts, and reproduction steps. Human review should target ambiguous or high-impact outcomes; do not mistake model agreement for ground truth. Publish failures as carefully as successes.

No leaderboard or vendor-comparison claims until independently reproducible test results exist.
