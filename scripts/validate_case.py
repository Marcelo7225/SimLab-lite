#!/usr/bin/env python
"""Validate structural completeness of a social-marketing-sim case."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FILES = [
    "00_brief.md",
    "01_social_map.md",
    "02_agents.json",
    "03_rounds.jsonl",
    "04_interviews.md",
    "05_causal_map.md",
    "06_prescriptions.md",
    "07_experiments.md",
    "08_war_room_final.md",
    "CASE_INDEX.md",
]


def nonempty(path: Path) -> bool:
    return path.exists() and path.read_text(encoding="utf-8").strip() != ""


def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            json.loads(line)
            count += 1
        except json.JSONDecodeError:
            pass
    return count


def count_markdown_sections(path: Path, marker: str) -> int:
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8").count(marker)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a social marketing simulation case.")
    parser.add_argument("case_dir")
    parser.add_argument("--min-agents", type=int, default=15)
    parser.add_argument("--min-rounds", type=int, default=3)
    parser.add_argument("--min-interviews", type=int, default=7)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    case_dir = Path(args.case_dir).resolve()
    missing = [name for name in REQUIRED_FILES if not (case_dir / name).exists()]
    empty = [name for name in REQUIRED_FILES if (case_dir / name).exists() and not nonempty(case_dir / name)]

    agent_count = 0
    agents_path = case_dir / "02_agents.json"
    if agents_path.exists():
        try:
            data = json.loads(agents_path.read_text(encoding="utf-8"))
            agents = data.get("agents", [])
            agent_count = len(agents) if isinstance(agents, list) else 0
            if not agent_count and isinstance(data.get("agent_count"), int):
                agent_count = data["agent_count"]
        except json.JSONDecodeError:
            missing.append("02_agents.json:invalid_json")

    round_count = count_jsonl(case_dir / "03_rounds.jsonl")
    interview_count = count_markdown_sections(case_dir / "04_interviews.md", "###")
    hypothesis_count = count_markdown_sections(case_dir / "05_causal_map.md", "###")
    prescription_count = count_markdown_sections(case_dir / "06_prescriptions.md", "###")
    experiment_count = count_markdown_sections(case_dir / "07_experiments.md", "## Experimento")

    checks = {
        "required_files_present": not missing,
        "required_files_nonempty": not empty,
        "agent_count_gte_min": agent_count >= args.min_agents,
        "round_count_gte_min": round_count >= args.min_rounds,
        "interview_count_gte_min": interview_count >= args.min_interviews,
        "has_causal_hypotheses": hypothesis_count >= 3,
        "has_prescriptions": prescription_count >= 3,
        "has_experiments": experiment_count >= 3,
    }
    score = round(sum(1 for ok in checks.values() if ok) / len(checks) * 100)
    result = {
        "case_dir": str(case_dir),
        "status": "complete" if all(checks.values()) else "incomplete",
        "completion_score": score,
        "checks": checks,
        "missing": missing,
        "empty": empty,
        "counts": {
            "agents": agent_count,
            "rounds": round_count,
            "interviews": interview_count,
            "causal_hypotheses": hypothesis_count,
            "prescriptions": prescription_count,
            "experiments": experiment_count,
        },
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"status: {result['status']}")
        print(f"completion_score: {score}")
        for key, ok in checks.items():
            print(f"{key}: {'ok' if ok else 'fail'}")
        if missing:
            print("missing:", ", ".join(missing))
        if empty:
            print("empty:", ", ".join(empty))

    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

