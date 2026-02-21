#!/bin/bash
# Pathology Skills Collection - Uninstallation Script

SYMLINK_PATH="$HOME/.claude/skills/pathology-skills-collection"

if [ -L "$SYMLINK_PATH" ]; then
    rm "$SYMLINK_PATH"
    echo "✓ Uninstalled pathology skills collection"
else
    echo "No installation found"
fi
