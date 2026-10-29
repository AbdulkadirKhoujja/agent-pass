"""Tests for the offline simulation; not a security audit or interoperability suite."""

import unittest

from mandovyn import describe, process, verify_demo_receipt


def valid_request():
    return {
        "agent_id": "test-agent",
        "action": "demo:read",
        "resource": "demo:catalog",
        "consent": True,
    }


class MandovynDemoTests(unittest.TestCase):
    def test_discovery_identifies_demo_limits(self):
        info = describe()
        self.assertEqual(info["kind"], "offline-simulator")
        self.assertFalse(info["identity_verification"])
        self.assertEqual(info["protocol_compliance"], [])

    def test_allowed_sample_is_simulated_only(self):
        response = process(valid_request())
        self.assertEqual(response["status"], "simulated")
        self.assertEqual(response["result"]["mode"], "synthetic-data")

    def test_denies_missing_test_consent(self):
        request = valid_request()
        request["consent"] = False
        self.assertEqual(process(request)["status"], "denied")

    def test_denies_unsupported_action(self):
        request = valid_request()
        request["action"] = "demo:delete"
        self.assertEqual(process(request)["status"], "denied")

    def test_denies_unsupported_resource(self):
        request = valid_request()
        request["resource"] = "real:bank-account"
        self.assertEqual(process(request)["status"], "denied")

    def test_denies_missing_agent_identifier(self):
        request = valid_request()
        request["agent_id"] = ""
        self.assertEqual(process(request)["status"], "denied")

    def test_rejects_non_object_request(self):
        self.assertEqual(process([])["status"], "denied")

    def test_checksum_consistent_for_untouched_receipt(self):
        receipt = process(valid_request())["receipt"]
        self.assertTrue(verify_demo_receipt(receipt))
        self.assertFalse(receipt["authenticity_verified"])

    def test_checksum_detects_accidental_result_change(self):
        receipt = process(valid_request())["receipt"]
        receipt["result"]["items"][0] = "changed"
        self.assertFalse(verify_demo_receipt(receipt))

    def test_checksum_does_not_represent_authentication(self):
        receipt = process(valid_request())["receipt"]
        self.assertIn("Not signed", receipt["note"])


if __name__ == "__main__":
    unittest.main()
