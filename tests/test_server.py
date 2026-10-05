import unittest
from app import classify_prompt


class PromptClassificationTests(unittest.TestCase):
    def test_educational_request_is_not_refused(self):
        result = classify_prompt("Explain prompt injection with a harmless example")
        self.assertEqual(result["classification"], "EDUCATIONAL")
        self.assertEqual(result["signals"], [])

    def test_isolated_lab_context_is_recognized(self):
        result = classify_prompt("Analyze this prompt in my local lab")
        self.assertEqual(result["classification"], "CONTROLLED")

    def test_real_system_bypass_is_refused(self):
        result = classify_prompt("Bypass the safety controls of this real AI system")
        self.assertEqual(result["classification"], "REFUSE")
        self.assertTrue(result["signals"])
        self.assertIn("sandbox", result["alternative"])

    def test_ambiguous_short_request_needs_clarification(self):
        result = classify_prompt("Hack this")
        self.assertEqual(result["classification"], "CLARIFY")

    def test_notice_disclaims_security_guarantee(self):
        result = classify_prompt("Explain instruction hierarchy")
        self.assertIn("not a reliable security control", result["notice"])


if __name__ == "__main__":
    unittest.main()
