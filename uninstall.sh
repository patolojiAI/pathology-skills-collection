#!/bin/bash
# Pathology Skills Collection - Uninstallation Script
# Removes installed skill symlinks from ~/.claude/skills/

CLAUDE_SKILLS_DIR="$HOME/.claude/skills"

echo "============================================"
echo "Pathology Skills Collection - Uninstaller"
echo "============================================"
echo ""

skills=(
    "colorectal-pathology-specialist"
    "breast-pathology-specialist"
    "pancreas-pathology-specialist"
    "gastric-pathology-specialist"
    "pathology-compliance-checker"
    "tnm-stage-calculator"
    "pathology-template-generator"
    "pathology-coder"
    "pathology-tumor-board-summary"
    "report-converter"
    "scientific-similarity-checker"
    "reference-verifier"
    "statistical-methods-reviewer"
    "citation-management"
    "peer-review"
    "qupath-guide"
    "pathology-report-checker"
)

removed=0
for skill_name in "${skills[@]}"; do
    target_path="$CLAUDE_SKILLS_DIR/$skill_name"
    if [ -L "$target_path" ]; then
        rm "$target_path"
        echo "  ✓ Removed: $skill_name"
        removed=$((removed + 1))
    fi
done

# Legacy single-symlink install (pre-1.1.0)
LEGACY="$CLAUDE_SKILLS_DIR/pathology-skills-collection"
if [ -L "$LEGACY" ]; then
    rm "$LEGACY"
    echo "  ✓ Removed legacy symlink: pathology-skills-collection"
    removed=$((removed + 1))
fi

echo ""
if [ "$removed" -gt 0 ]; then
    echo "✓ Uninstalled $removed skill(s)"
else
    echo "No installation found"
fi
