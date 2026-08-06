#!/usr/bin/env python
"""Create a local case folder for the social-marketing-sim skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "marketing-sim-case"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a social marketing simulation case.")
    parser.add_argument("case_name", help="Case name or slug")
    parser.add_argument("--root", default="cases", help="Root directory for cases")
    parser.add_argument("--agents", type=int, default=18, help="Default target agent count")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files")
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "assets" / "templates"
    case_slug = slugify(args.case_name)
    case_dir = Path(args.root).resolve() / case_slug
    memory_dir = case_dir / "memory"

    case_dir.mkdir(parents=True, exist_ok=True)
    memory_dir.mkdir(parents=True, exist_ok=True)

    for template in template_dir.iterdir():
        if template.is_file():
            dest = case_dir / template.name
            if args.force or not dest.exists():
                shutil.copyfile(template, dest)

    now = utc_now()
    session_id = hashlib.sha1(f"{case_slug}:{now}".encode("utf-8")).hexdigest()[:12]
    session = {
        "session_id": session_id,
        "case_name": args.case_name,
        "case_slug": case_slug,
        "created_at": now,
        "updated_at": now,
        "status": "initialized",
        "current_stage": "brief",
        "completed_stages": [],
        "target_agent_count": args.agents,
        "simulation_round_count": 0,
        "interview_count": 0,
        "completion_score": 0,
    }

    session_path = case_dir / "session.json"
    if args.force or not session_path.exists():
        session_path.write_text(json.dumps(session, ensure_ascii=False, indent=2), encoding="utf-8")

    memory_files = {
        "facts.json": [],
        "assumptions.json": [],
        "unresolved_questions.json": [],
    }
    for filename, payload in memory_files.items():
        path = memory_dir / filename
        if args.force or not path.exists():
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    for filename in ["decisions.jsonl", "checkpoints.jsonl"]:
        path = memory_dir / filename
        if args.force or not path.exists():
            path.write_text("", encoding="utf-8")

    print(str(case_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
