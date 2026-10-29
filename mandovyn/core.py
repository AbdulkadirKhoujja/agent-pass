"""Deterministic, offline demonstration of an agent permission flow.

SECURITY NOTICE:
- agent_id is merely an unverified string and proves no identity.
- consent is a caller-supplied test boolean; not actual user consent.
- no network or external actions are performed.
- receipt digests are NOT signed and provide NO authenticity guarantee.
"""

import hashlib
import hmac
import json
from typing import Any

_DEMO_ITEMS = ["alpha", "beta"]


def describe() -> dict[str, Any]:
    """Discovery document for the local simulator (not an A2A Agent Card)."""
    return {
        "name": "Mandovyn demo",
        "version": "0.1.0",
        "kind": "offline-simulator",
        "supported_action": "demo:read",
        "supported_resource": "demo:catalog",
        "identity_verification": False,
        "real_user_consent": False,
        "external_actions": False,
        "protocol_compliance": [],
    }


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _checksum(request: dict[str, Any], result: dict[str, Any]) -> str:
    payload = {"request": request, "result": result}
    return hashlib.sha256(_canonical(payload).encode("utf-8")).hexdigest()


def process(request: Any) -> dict[str, Any]:
    """Evaluate an untrusted sample request, without any real-world effects."""
    if not isinstance(request, dict):
        return {"status": "denied", "reason": "request must be a JSON object"}

    if not isinstance(request.get("agent_id"), str) or not request["agent_id"].strip():
        return {"status": "denied", "reason": "agent_id must be a nonempty string"}
    if request.get("action") != "demo:read":
        return {"status": "denied", "reason": "action is not permitted in the demo"}
    if request.get("resource") != "demo:catalog":
        return {"status": "denied", "reason": "resource is not permitted in the demo"}
    if request.get("consent") is not True:
        return {"status": "denied", "reason": "explicit test-consent flag is required"}

    # No actual identity, authority, signature or delegated consent is verified.
    result = {"items": list(_DEMO_ITEMS), "mode": "synthetic-data"}
    receipt = {
        "kind": "mandovyn-demo-checksum",
        "request": dict(request),
        "result": result,
        "checksum_sha256": _checksum(request, result),
        "authenticity_verified": False,
        "note": "Checksum only. Not signed, not a real authorization or receipt.",
    }
    return {
        "status": "simulated",
        "decision": "allowed-by-local-demo-policy",
        "result": result,
        "receipt": receipt,
    }


def verify_demo_receipt(receipt: Any) -> bool:
    """Check only internal consistency; does NOT authenticate a receipt."""
    if not isinstance(receipt, dict):
        return False
    if receipt.get("kind") != "mandovyn-demo-checksum":
        return False
    request = receipt.get("request")
    result = receipt.get("result")
    checksum = receipt.get("checksum_sha256")
    if not isinstance(request, dict) or not isinstance(result, dict):
        return False
    if not isinstance(checksum, str) or len(checksum) != 64:
        return False
    return hmac.compare_digest(checksum, _checksum(request, result))
