"""Run the offline Mandovyn simulator."""

import argparse
import json
from pathlib import Path

from .core import describe, process


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline Mandovyn demo; no real authorizations")
    parser.add_argument("request_json", nargs="?", type=Path, help="Path to an example JSON request")
    parser.add_argument("--describe", action="store_true", help="Print demo discovery capabilities")
    args = parser.parse_args()

    if args.describe:
        output = describe()
    elif args.request_json:
        try:
            output = process(json.loads(args.request_json.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError) as exc:
            parser.error(str(exc))
    else:
        output = process({
            "agent_id": "example-agent-unverified",
            "action": "demo:read",
            "resource": "demo:catalog",
            "consent": True,
        })

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
