# Contributing to Mandovyn

Thanks for contributing to a small, independent open-source experiment.

## Good first contributions

- Threat-model a narrow feature and propose negative tests.
- Improve accessibility or clarity of the docs and landing page.
- Add JSON validation, malformed-input tests, and explicit security disclaimers.
- Improve reproducible benchmarking with fixed synthetic fixtures.
- Research a **specific** AuthZEN, A2A, or MCP interoperability gap and link to authoritative specification text.
- Propose an upstream fix to another open-source project **on its own merits**, without product promotion.

## Development

1. Fork or open a branch; keep changes small and reviewable.
2. Run `python -m unittest discover -s tests -v` (Python 3.10+).
3. Add tests for changed behaviour, especially denied and malformed requests.
4. Explain limitations and avoid claiming real identity verification or compliance.
5. Submit a PR with the change, risk, tests, and evidence.

## Contribution boundaries

Do not add credentials, personal/client data, generated spam, background web crawlers, mass outreach, benchmark claims without traceable fixtures, fake receipts, or alleged official standard endorsements. Do not contact upstream maintainers on Mandovyn's behalf without a relevant contribution ready for review.

Project participation is governed by respectful, civil collaboration. Substantial protocol changes require a design issue and maintainer approval before merger.

Contributions are made under the repository's Apache-2.0 license.
