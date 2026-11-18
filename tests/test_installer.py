"""Network-free tests for installer guardrails."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "tools" / "meteomatrix.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class GuardrailTests(unittest.TestCase):
    def test_digest(self):
        self.assertEqual(installer.digest(b"abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_api_error_in_http_200(self):
        with self.assertRaises(RuntimeError):
            installer.parse_response(200, b'{"ok":true,"error":{"message":"compile error"}}')

    def test_valid_api_success(self):
        self.assertTrue(installer.parse_response(200, b'{"ok":true,"error":null}')["ok"])

    def test_http_failure(self):
        with self.assertRaises(RuntimeError):
            installer.parse_response(404, b'{"ok":false}')

    def test_source_has_config(self):
        source = (ROOT / "src" / "MeteoMatrix.ax").read_text(encoding="utf-8")
        self.assertIn('# @config latitude', source)
        self.assertIn('# @config longitude', source)
        self.assertIn('store.get("timezone")', source)

    def test_bitmap_preservation(self):
        original = (ROOT / "src" / "legacy" / "SieradzMeteo_v1_5.ax").read_text(encoding="utf-8")
        derived = (ROOT / "src" / "MeteoMatrix.ax").read_text(encoding="utf-8")
        import re
        pattern = r'self\.glyphs = \[[\s\S]*?\n    \]'
        self.assertEqual(re.search(pattern, original).group(), re.search(pattern, derived).group())


if __name__ == "__main__":
    unittest.main()
