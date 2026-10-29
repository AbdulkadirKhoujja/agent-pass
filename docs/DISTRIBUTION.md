# Distribution plan: build the flywheel into the product

## Operating allocation

**70% product:** useful capabilities, developer experience, docs, verified integrations, testable releases, and feedback-driven fixes.

**30% ecosystem:** upstream contributions, interoperability, open documentation, benchmarks, useful replies and opt-in community relationships.

These are planning allocations, not a claim of time already spent or conversion performance.

## Distribution channels

| Channel | What we ship | Evidence we need |
| --- | --- | --- |
| GitHub discovery | Clear README, license, topics, issues, source code, release tags | Views/stars/forks and meaningful issues |
| Developer-led adoption | Dependency-free sample, SDK after validation, copyable examples | Successful first-run and repeat usage |
| Search / AEO / GEO | Search-readable landing page; truthful FAQ and `llms.txt` | Search impressions, referral visits, indexed URLs |
| Machine-readable discovery | Accurate metadata and endpoint docs for implemented interfaces | Third-party clients can discover and invoke live interfaces |
| Protocol ecosystem | Small maintainer-relevant AuthZEN / A2A / MCP contributions | Merged, useful upstream PRs and independently reported findings |
| Benchmarks | Pinned synthetic fixtures and real-world evals only when permitted | Public reproducible scripts, exact baselines and limitations |
| Community | Helpful replies to user questions and opt-in announcements | GitHub issues, substantive inbound contributions |

## First 30 days

**Week 1:** publish the starter, verify CI and GitHub Pages, add reproducible examples, and review product scope. Capture baseline metrics (even when zero).

**Week 2:** expand negative tests, threat model and schema validation. Find one upstream issue that genuinely benefits from a self-contained fix.

**Week 3:** produce a narrow, independently reproducible interoperability example; request maintainer feedback before presenting it as compatible.

**Week 4:** publish a factual build log and benchmark methodology. Share only authentic findings in suitable channels, following community rules.

## Content plan (non-spam)

- Article: “What an AI agent should prove before acting.”
- Demo: “A denied action is a successful safety test.”
- Technical note: “Why an unsigned hash is not an authenticated receipt.”
- Comparison: “Authorization vs discovery: AuthZEN, A2A and MCP solve different layers.”
- Tutorial: “Run the AgentPass offline simulator in 60 seconds.”

Every post links to a working demonstration and states current limitations. Do not mass-post identical text, manipulate search, fabricate adoption, or create standards-affiliation confusion.

## Measurement discipline

Track: traffic source → README or docs view → first demo run → repeat use → meaningful issue/PR → compatible integration. Label all numbers as measured, estimated, or unavailable. Do not confuse stars with active users or synthetic tests with production proof.

## Critical bottleneck

A GitHub repository is **not** distribution on its own. Before making product claims, independently verify live endpoint behavior, human consent, security, and adoption. Never claim an MCP or A2A registration just because metadata was written in a file.
