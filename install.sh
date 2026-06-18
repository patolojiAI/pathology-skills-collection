#!/bin/bash
# Pathology Skills Collection - Installer
# Installs individual skills to ~/.claude/skills/ as symlinks.
#
# Folder name and SKILL.md `name:` field are identical for every skill, so
# the installer simply mirrors each folder under ~/.claude/skills/.

set -e

SKILLS_DIR="$(cd "$(dirname "$0")" && pwd)/pathology-skills"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"

echo "============================================"
echo "Pathology Skills Collection - Installer"
echo "============================================"
echo ""

mkdir -p "$CLAUDE_SKILLS_DIR"

echo "Installing skills to $CLAUDE_SKILLS_DIR..."
echo ""

skills=(
    "breast-pathology-specialist"
    "colorectal-pathology-specialist"
    "gastric-pathology-specialist"
    "pancreas-pathology-specialist"
    "pathology-compliance-checker"
    "pathology-template-generator"
    "pathology-tumor-board-summary"
    "pathology-coder"
    "tnm-stage-calculator"
    "report-converter"
    "scientific-similarity-checker"
    "reference-verifier"
    "statistical-methods-reviewer"
    "citation-management"
    "peer-review"
    "qupath-guide"
    "pathology-report-checker"
)

for skill in "${skills[@]}"; do
    source_path="$SKILLS_DIR/$skill"
    target_path="$CLAUDE_SKILLS_DIR/$skill"

    if [ -L "$target_path" ]; then
        echo "  Replacing existing symlink: $skill"
        rm "$target_path"
    elif [ -e "$target_path" ]; then
        echo "  ✗ Skipping $skill (target exists and is not a symlink)"
        continue
    fi

    if [ -d "$source_path" ]; then
        ln -s "$source_path" "$target_path"
        echo "  ✓ Installed: $skill"
    else
        echo "  ✗ Source not found: $source_path (skipping)"
    fi
done

echo ""
echo "============================================"
echo "✓ Installation Complete (${#skills[@]} skills)"
echo "============================================"
echo ""
echo "Test installation:"
echo "  claude 'List available skills'"
echo ""
echo "Use a skill:"
echo "  claude 'Use colorectal-pathology-specialist to analyze report' < report.txt"
echo ""
