#!/usr/bin/env python3
"""Read-only English prose heuristics, not factual or submission certification."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class Finding:
    code: str
    paragraph: int
    line: int
    message: str
    excerpt: str


def prose_paragraphs(text: str) -> list[tuple[int, str]]:
    """Return paragraph-start line numbers and prose, excluding Markdown scaffolding."""
    paragraphs: list[tuple[int, str]] = []
    current: list[str] = []
    start = 0
    fence_char = ""
    fence_length = 0
    lines = text.splitlines()
    frontmatter = False
    if lines and lines[0].strip() == "---":
        for end in range(1, len(lines)):
            if lines[end].strip() in {"---", "..."}:
                frontmatter = any(re.match(r"^[A-Za-z_][\w-]*\s*:", value) for value in lines[1:end])
                break

    def flush() -> None:
        nonlocal current
        if current:
            paragraphs.append((start, " ".join(current)))
            current = []

    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if frontmatter:
            if number > 1 and stripped in {"---", "..."}:
                frontmatter = False
            continue
        fence = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            marker, tail = fence.groups()
            if not fence_char:
                flush()
                fence_char, fence_length = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length and not tail.strip():
                fence_char = ""
                fence_length = 0
            continue
        if fence_char:
            continue
        if not stripped or stripped.startswith(("#", "|")) or stripped == "---":
            flush()
            continue
        if not current:
            start = number
        current.append(stripped)
    flush()
    return paragraphs


def review_text(text: str, long_sentence_words: int = 55) -> dict:
    """Report contextual review prompts without modifying text or asserting quality."""
    if long_sentence_words < 1:
        raise ValueError("long_sentence_words must be positive")
    paragraphs = prose_paragraphs(text)
    findings: list[Finding] = []
    seen_sentences: dict[str, int] = {}
    connective_occurrences: dict[str, list[tuple[int, int, str]]] = {}
    patterns = (
        (
            "defensive_formula",
            re.compile(r"\b(?:to avoid misunderstanding|it should be (?:noted|emphasized) that|we do not claim that)\b", re.I),
            "Check whether this can state the definition or limitation directly; retain any necessary qualification.",
        ),
        (
            "opaque_label",
            re.compile(r"\b(?:jointly qualifying|destination[- ]area conditions|various stakeholders)\b", re.I),
            "Check that the relevant criteria, place, or responsible actor are already clear; do not repeat a definition unnecessarily.",
        ),
        (
            "inflated_contribution",
            re.compile(r"\b(?:revolutionary (?:framework|paradigm)|completely transforms|unprecedented breakthrough)\b", re.I),
            "Name the actual analytical or conceptual advance and check that the evidence supports its scope.",
        ),
    )
    for index, (line, paragraph) in enumerate(paragraphs, 1):
        for code, pattern, message in patterns:
            if pattern.search(paragraph):
                findings.append(Finding(code, index, line, message, paragraph[:220]))
        counts = Counter(re.findall(r"\b(?:therefore|thus|hence|consequently)\b", paragraph, re.I))
        for word, count in counts.items():
            connective_occurrences.setdefault(word.lower(), []).extend([(index, line, paragraph)] * count)
        for sentence in re.split(r'(?<=[.!?])\s+(?=[A-Z“"])', paragraph):
            words = re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", sentence)
            if len(words) > long_sentence_words:
                findings.append(Finding(
                    "long_sentence", index, line,
                    f"This sentence has {len(words)} words; check the reading load, not a mandatory length limit.",
                    sentence[:220],
                ))
            normalized = " ".join(word.lower() for word in words)
            if len(words) >= 8:
                if normalized in seen_sentences:
                    findings.append(Finding(
                        "repeated_sentence", index, line,
                        f"A normalized sentence also appears in paragraph {seen_sentences[normalized]}; check whether the repetition has a distinct job.",
                        sentence[:220],
                    ))
                else:
                    seen_sentences[normalized] = index
    for word, occurrences in connective_occurrences.items():
        for start, (index, line, paragraph) in enumerate(occurrences):
            nearby = [item for item in occurrences[start:] if item[0] <= index + 4]
            if len(nearby) >= 3:
                findings.append(Finding(
                    "repeated_causal_connective", index, line,
                    f"'{word}' appears {len(nearby)} times within paragraphs {index}-{nearby[-1][0]}; review the argument and cadence before changing any connector.",
                    paragraph[:220],
                ))
                break
    return {
        "assessment": "heuristic_review_only",
        "scope": "English prose patterns; no citation, empirical, Word-layout, or submission verification",
        "location_note": "Line numbers identify paragraph starts, not exact sentence offsets.",
        "paragraphs_reviewed": len(paragraphs),
        "findings": [asdict(finding) for finding in findings],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("path", nargs="?", type=Path, help="UTF-8 .txt or .md draft")
    source.add_argument("--text", help="Review supplied text without creating a file")
    parser.add_argument("--json", action="store_true", help="Print a JSON report to standard output")
    parser.add_argument("--long-sentence-words", type=int, default=55, help="Advisory threshold, default 55")
    args = parser.parse_args(argv)
    if args.long_sentence_words < 1:
        parser.error("--long-sentence-words must be positive")
    if args.path is not None:
        if args.path.suffix.lower() not in {".txt", ".md"}:
            parser.error("Only UTF-8 .txt and .md are supported; use a document reader for Word files.")
        try:
            text = args.path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as error:
            parser.exit(2, f"Cannot read input: {error}\n")
    else:
        text = args.text
    result = review_text(text, args.long_sentence_words)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Contextual review prompts only; no automatic quality or submission decision.")
        print(f"Paragraphs reviewed: {result['paragraphs_reviewed']}")
        if not result["findings"]:
            print("No matches for these limited heuristics. This does not establish prose or research quality.")
        for finding in result["findings"]:
            print(f"Paragraph {finding['paragraph']} (starts line {finding['line']}), {finding['code']}: {finding['message']}")
            print(f"  {finding['excerpt']}")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
