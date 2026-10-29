# Mandovyn FAQ

**What is Mandovyn?** An open-source experiment in AI-agent discovery, authorized actions and receipts. The current Python demonstration is entirely offline and uses synthetic data.

**Is Mandovyn usable for real authentication?** No. The initial `agent_id` and `consent` fields are caller-supplied test inputs, not evidence.

**Does it support MCP or A2A today?** No. No compatible MCP server or A2A service has been deployed or registered.

**Are its receipts signed or authenticated?** No. The checksum demonstrates consistency only; anyone can recompute it.

**Can I build on the code?** Yes, under Apache-2.0, but do not treat the demonstration as production-security software.

**How is the project distributed?** The 70/30 strategy prioritizes useful product work alongside legitimate independent upstream contributions. We reject mass spam and misleading interoperability claims.

**Where are the reproducible results?** See [BENCHMARKS.md](BENCHMARKS.md) and the repository's unit tests. Public claims are restricted to fixtures actually run.
