#!/bin/bash
# Pathology Skills Collection - Installer
# Installs individual skills to ~/.claude/skills/

set -e

SKILLS_DIR="$(cd "$(dirname "$0")" && pwd)/pathology-skills"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"

echo "============================================"
echo "Pathology Skills Collection - Installer"
echo "============================================"
echo ""

# Create Claude skills directory if it doesn't exist
mkdir -p "$CLAUDE_SKILLS_DIR"

echo "Installing skills to $CLAUDE_SKILLS_DIR..."
echo ""

# Install each skill with proper naming (matches SKILL.md name field)
skills=(
    "colorectal-specialist:colorectal-pathology-specialist"
    "breast-specialist:breast-pathology-specialist"
    "pancreas-specialist:pancreas-pathology-specialist"
    "gastric-specialist:gastric-pathology-specialist"
    "compliance-checker:pathology-compliance-checker"
    "tnm-stage-calculator:tnm-stage-calculator"
    "template-generator:pathology-template-generator"
    "pathology-coder:pathology-coder"
    "tumor-board-summary:pathology-tumor-board-summary"
    "report-converter:report-converter"
    "scientific-similarity-checker:scientific-similarity-checker"
    "reference-verifier:reference-verifier"
)

for skill_mapping in "${skills[@]}"; do
    IFS=':' read -r folder_name skill_name <<< "$skill_mapping"
    source_path="$SKILLS_DIR/$folder_name"
    target_path="$CLAUDE_SKILLS_DIR/$skill_name"

    # Remove existing symlink if present
    if [ -L "$target_path" ]; then
        echo "  Removing old: $skill_name"
        rm "$target_path"
    fi

    # Create symlink
    if [ -d "$source_path" ]; then
        ln -s "$source_path" "$target_path"
        echo "  ✓ Installed: $skill_name"
    else
        echo "  ✗ Not found: $folder_name (skipping)"
    fi
done

echo ""
echo "============================================"
echo "✓ Installation Complete!"
echo "============================================"
echo ""
echo "Installed skills:"
ls -1 "$CLAUDE_SKILLS_DIR" | grep -E "pathology|tnm|report-converter|scientific-similarity-checker|reference-verifier" || echo "  (none found)"
echo ""
echo "Test installation:"
echo "  claude 'List available skills'"
echo ""
echo "Use a skill:"
echo "  claude 'Use colorectal-pathology-specialist to analyze report' < report.txt"
echo ""
