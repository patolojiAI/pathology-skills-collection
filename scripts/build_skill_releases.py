#!/usr/bin/env python3
"""Build standalone .skill release archives for every skill in pathology-skills/.

Each .skill file is a zip of a single skill folder, structured so the skill
runs correctly when uploaded via Claude.ai → Settings → Capabilities → Skills
(or the Claude desktop app). To make that work, this script:

  1. Copies the skill folder to a temp staging directory.
  2. Scans SKILL.md and every file under references/ for references to
     ../../shared-references/<path>.
  3. Copies each referenced shared-references file into the skill at
     references/_shared/<original-subpath>.
  4. Rewrites those paths in-place so the SKILL.md and reference files point
     at the now-bundled copy instead of the cross-skill path.
  5. Zips the staged folder as dist/<skill-name>.skill.

Bundled .skill files are self-contained and require no external paths.

Usage:
    python3 scripts/build_skill_releases.py
        # builds dist/<skill>.skill for every skill in pathology-skills/

    python3 scripts/build_skill_releases.py breast-pathology-specialist
        # builds only the named skill

The script is idempotent. dist/ is wiped at the start of each full build.
"""

from __future__ import annotations

import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO / "pathology-skills"
SHARED_DIR = REPO / "shared-references"
DIST_DIR = REPO / "dist"

# Matches ../../shared-references/<path> in markdown text or code spans.
SHARED_REF_RE = re.compile(r"\.\./\.\./shared-references/([^\s\`'\"\)]+)")


def stage_skill(skill_dir: Path, staging_root: Path) -> Path:
    """Copy the skill folder into staging_root, return the staged path."""
    target = staging_root / skill_dir.name
    shutil.copytree(skill_dir, target)
    return target


def collect_shared_refs(staged: Path) -> set[str]:
    """Find every ../../shared-references/<path> mentioned anywhere in the skill."""
    refs: set[str] = set()
    for path in staged.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".txt", ".py", ".sh"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for m in SHARED_REF_RE.finditer(content):
            refs.add(m.group(1))
    return refs


def inline_shared_refs(staged: Path, refs: set[str]) -> list[str]:
    """Copy each shared-references/<sub> into <staged>/references/_shared/<sub>.

    Returns a list of refs that could not be resolved (missing source files).
    """
    missing: list[str] = []
    for sub in sorted(refs):
        src = SHARED_DIR / sub
        if not src.is_file():
            missing.append(sub)
            continue
        dest = staged / "references" / "_shared" / sub
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    return missing


def rewrite_paths(staged: Path) -> None:
    """Rewrite ../../shared-references/<x> -> references/_shared/<x> in every text file."""
    for path in staged.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".txt", ".py", ".sh"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = SHARED_REF_RE.sub(r"references/_shared/\1", text)
        if new != text:
            path.write_text(new, encoding="utf-8")


def zip_skill(staged: Path, out_path: Path) -> None:
    """Zip the staged folder as a .skill archive."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(staged.rglob("*")):
            if path.is_dir():
                continue
            arcname = path.relative_to(staged.parent)
            zf.write(path, arcname)


def build_one(skill_dir: Path) -> tuple[Path, list[str]]:
    """Build one .skill release; return (output_path, missing_refs)."""
    name = skill_dir.name
    out_path = DIST_DIR / f"{name}.skill"

    with tempfile.TemporaryDirectory(prefix=f"skill-build-{name}-") as tmp:
        staging_root = Path(tmp)
        staged = stage_skill(skill_dir, staging_root)
        refs = collect_shared_refs(staged)
        missing = inline_shared_refs(staged, refs)
        rewrite_paths(staged)
        zip_skill(staged, out_path)

    return out_path, missing


def main(argv: list[str]) -> int:
    if not SKILLS_DIR.is_dir():
        print(f"error: {SKILLS_DIR} not found", file=sys.stderr)
        return 1

    if len(argv) > 1:
        skills = [SKILLS_DIR / a for a in argv[1:]]
        for s in skills:
            if not s.is_dir():
                print(f"error: skill folder {s} not found", file=sys.stderr)
                return 1
    else:
        skills = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
        if DIST_DIR.exists():
            shutil.rmtree(DIST_DIR)

    total_missing: dict[str, list[str]] = {}
    for skill_dir in skills:
        out, missing = build_one(skill_dir)
        size_kb = out.stat().st_size / 1024
        print(f"  ✓ {out.name:<48s} {size_kb:>7.1f} KB")
        if missing:
            total_missing[skill_dir.name] = missing

    print()
    print(f"Built {len(skills)} .skill file(s) → {DIST_DIR.relative_to(REPO)}/")

    if total_missing:
        print()
        print("WARNING: the following shared-references paths were referenced but")
        print("could not be found and were left as broken references in the bundle:")
        for skill, refs in total_missing.items():
            print(f"  {skill}:")
            for r in refs:
                print(f"    - shared-references/{r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
