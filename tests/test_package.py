"""Check discoverability and self-contained documentation, not preferred phrasing."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "brad-ssci-writing"


class PackageTests(unittest.TestCase):
    def test_skill_has_discoverable_name_and_description(self):
        content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", content, re.S)
        self.assertIsNotNone(match)
        self.assertIn("name: brad-ssci-writing", match.group(1))
        self.assertIn("description:", match.group(1))
        self.assertNotIn("[TODO:", content)

    def test_local_documentation_links_resolve_inside_repo(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (path, target))
                self.assertTrue(resolved.is_file(), (path, target))

    def test_ui_prompt_invokes_the_skill(self):
        content = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$brad-ssci-writing", content)
        self.assertNotIn("allow_implicit_invocation: false", content)

    def test_payload_contains_no_manuscript_or_binary_artifacts(self):
        forbidden = {".doc", ".docx", ".pdf", ".pptx", ".xlsx", ".csv", ".sqlite", ".pkl", ".gpkg"}
        for path in SKILL.rglob("*"):
            if path.is_file():
                self.assertNotIn(path.suffix.lower(), forbidden, path)


if __name__ == "__main__":
    unittest.main()
