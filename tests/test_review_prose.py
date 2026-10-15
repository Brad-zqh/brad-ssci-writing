"""Synthetic behavioral tests; no manuscript or research data are used."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "brad-ssci-writing" / "scripts" / "review_prose.py"
SPEC = importlib.util.spec_from_file_location("review_prose", SCRIPT)
prose = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prose
SPEC.loader.exec_module(prose)


class ReviewProseTests(unittest.TestCase):
    def codes(self, text):
        return [finding["code"] for finding in prose.review_text(text)["findings"]]

    def test_ordinary_research_prose_has_no_required_rewrite(self):
        self.assertEqual(self.codes("We compared service conditions across the study areas. The analysis used the same definitions in each year."), [])

    def test_parallel_signposts_are_allowed(self):
        text = "First, we defined the construct.\n\nSecond, we compared the observations.\n\nThird, we discussed the implications."
        self.assertEqual(self.codes(text), [])

    def test_one_therefore_is_not_forbidden(self):
        self.assertEqual(self.codes("The fees varied between sites. We therefore examined the price categories."), [])

    def test_three_connectives_raise_a_contextual_prompt(self):
        result = prose.review_text("We therefore examined fees.\n\nWe therefore examined distance.\n\nWe therefore examined service hours.")
        self.assertIn("repeated_causal_connective", [item["code"] for item in result["findings"]])
        self.assertEqual(result["assessment"], "heuristic_review_only")
        self.assertNotIn("score", result)

    def test_duplicate_sentence_is_located(self):
        sentence = "We compared the distribution of services across the study areas."
        result = prose.review_text(sentence + "\n\n" + sentence)
        duplicate = next(item for item in result["findings"] if item["code"] == "repeated_sentence")
        self.assertEqual((duplicate["paragraph"], duplicate["line"]), (2, 3))

    def test_connectives_spread_across_a_long_draft_are_not_automatically_flagged(self):
        paragraphs = [f"This section examines service category {number}." for number in range(15)]
        for index in (0, 7, 14):
            paragraphs[index] = f"We therefore examine service category {index}."
        self.assertNotIn("repeated_causal_connective", self.codes("\n\n".join(paragraphs)))

    def test_markdown_code_and_frontmatter_are_not_prose(self):
        text = "---\nname: therefore therefore therefore\n---\n\n```text\nto avoid misunderstanding\n```\n\nWe examined service hours."
        result = prose.review_text(text)
        self.assertEqual(result["paragraphs_reviewed"], 1)
        self.assertEqual(result["findings"], [])

    def test_false_closing_fence_does_not_expose_code(self):
        text = "````text\n```\ntherefore therefore therefore\n````\n\nWe examined service hours."
        self.assertEqual(self.codes(text), [])

    def test_leading_horizontal_rule_does_not_hide_prose(self):
        result = prose.review_text("---\n\nWe examined service hours.")
        self.assertEqual(result["paragraphs_reviewed"], 1)
        self.assertEqual(result["findings"], [])

    def test_necessary_negative_statement_is_not_defensive_formula(self):
        self.assertEqual(self.codes("The indicator measures reachable options rather than observed visits."), [])

    def test_warning_does_not_mutate_text_or_force_failure(self):
        text = "To avoid misunderstanding, we explain the indicator."
        original = text
        self.assertIn("defensive_formula", self.codes(text))
        self.assertEqual(text, original)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            status = prose.main(["--text", text, "--json"])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output.getvalue())["assessment"], "heuristic_review_only")

    def test_long_sentence_threshold_is_advisory(self):
        self.assertIn("long_sentence", [item["code"] for item in prose.review_text("We compared several local services across the study areas.", 5)["findings"]])
        with self.assertRaises(ValueError):
            prose.review_text("Text.", 0)

    def test_cli_rejects_word_without_reading_it(self):
        process = subprocess.run([sys.executable, "-B", str(SCRIPT), "unused.docx", "--json"], capture_output=True, text=True)
        self.assertEqual(process.returncode, 2)
        self.assertIn("document reader", process.stderr)

    def test_cli_read_only_file_input(self):
        with tempfile.TemporaryDirectory(prefix="brad-skill-test-") as temporary:
            path = Path(temporary) / "draft.md"
            original = b"We compared service hours across the study areas.\n"
            path.write_bytes(original)
            process = subprocess.run([sys.executable, "-B", str(SCRIPT), str(path), "--json"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(json.loads(process.stdout)["assessment"], "heuristic_review_only")
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(list(Path(temporary).iterdir()), [path])


if __name__ == "__main__":
    unittest.main()
