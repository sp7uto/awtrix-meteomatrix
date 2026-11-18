"""Network-free tests for installer guardrails."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
import argparse
import tempfile

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
        original = (ROOT / "src" / "legacy" / "SieradzMeteo_v1_6.ax").read_text(encoding="utf-8")
        derived = (ROOT / "src" / "MeteoMatrix.ax").read_text(encoding="utf-8")
        import re
        pattern = r'self\.glyphs = \[[\s\S]*?\n\s*\]'
        self.assertEqual(re.search(pattern, original).group(), re.search(pattern, derived).group())

    def test_language_switch(self):
        source = (ROOT / "src" / "MeteoMatrix.ax").read_text(encoding="utf-8")
        self.assertIn('# @config language select', source)
        self.assertIn('store.get("language")', source)
        self.assertIn('self.tr("DESZCZ ","RAIN ")', source)
        self.assertIn("def draw_event()", source)
        self.assertIn("def draw_phase()", source)

    def test_dry_run_makes_no_write(self):
        args = argparse.Namespace(name="MeteoMatrix", user=None, host="http://test.invalid",
                                  command="install", file=ROOT / "src" / "MeteoMatrix.ax",
                                  backup_dir=ROOT / "backups", apply=False)
        with patch.object(installer, "get_script", return_value=None):
            with patch.object(installer, "request") as mocked:
                installer.run(args)
                mocked.assert_not_called()

    def test_atomic_create_uses_expected_null(self):
        args = argparse.Namespace(name="MeteoMatrix", user=None, host="http://test.invalid",
                                  command="install", file=ROOT / "src" / "MeteoMatrix.ax",
                                  backup_dir=ROOT / "backups", apply=True)
        data = args.file.read_bytes()
        with patch.object(installer, "get_script", side_effect=[None, data]):
            with patch.object(installer, "request", return_value=(200, b'{"ok":true}')) as mocked:
                installer.run(args)
        kwargs = mocked.call_args.kwargs
        self.assertEqual(kwargs["method"], "PUT")
        self.assertEqual(kwargs["body"]["expected_source"], None)
        self.assertIn("/api/v1/apps/script-update/MeteoMatrix", mocked.call_args.args[1])

    def test_backup_creates_private_file(self):
        with tempfile.TemporaryDirectory() as folder:
            file = installer.backup(b"original code", "MeteoMatrix", Path(folder))
            self.assertEqual(file.read_bytes(), b"original code")
            self.assertEqual(file.stat().st_mode & 0o777, 0o600)


if __name__ == "__main__":
    unittest.main()
