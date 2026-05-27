---
name: qupath-guide
description: Guides QuPath users in digital pathology with troubleshooting, interface navigation, image analysis workflows, and Groovy scripting. Use when the user mentions QuPath, or uses QuPath-specific signals such as .qpproj/.qpdata files, "Run for Project", "stain vectors", "TMA dearrayer", "detection objects", or "Brightfield (H-DAB)". Also use for QuPath cell detection, tissue/tumor annotation, IHC scoring (Ki-67, HER2, PD-L1), stain separation/deconvolution, pixel or object classification, TMA analysis, multiplex/mIF analysis, Groovy scripts for pathology slides, measurement export, batch processing, QuPath extensions, or QuPath errors. Provides menu paths, workflows, ready-to-run Groovy snippets, and fetches official QuPath docs for version-specific details. Do NOT use for general non-QuPath image processing, ImageJ/Fiji-only questions, or standalone deep-learning pipelines (e.g. StarDist/Cellpose in plain Python) outside QuPath.
license: MIT
compatibility: "Works across Claude.ai, Claude Code, and API. Benefits from web access to fetch official QuPath documentation (qupath.readthedocs.io, javadoc, forum.image.sc) for version-specific details. Guidance targets QuPath 0.5.x and 0.6.x; current stable release is 0.6.0."
metadata:
  version: 2.1.0
  author: Serdar Balci
  domain: digital-pathology
  tags: [qupath, digital-pathology, groovy, image-analysis, ihc]
---

# QuPath Guide

Help users get the most out of QuPath — the open-source platform for bioimage analysis widely used
in digital pathology research. This skill covers troubleshooting, interface navigation, image
analysis workflows, and Groovy scripting.

## Approach

When a user asks a QuPath question, follow this decision flow:

1. **Assess the user's level** from context cues (terminology, question complexity, error messages).
   Adapt language accordingly — a pathologist new to QuPath needs different guidance than a developer
   building extensions.

2. **Identify the category** of the question:
   - **Troubleshooting** → Read `references/troubleshooting.md` first. Most users come with a problem.
   - **UI / Navigation** → Read `references/ui-guide.md` for interface guidance.
   - **Analysis workflows** → Read `references/analysis-workflows.md` for step-by-step workflows.
   - **Scripting** → Read `references/scripting-guide.md` for Groovy patterns and examples.
   - **Multiple categories** → Read the relevant reference files in combination.

3. **Fetch official docs when needed.** For version-specific details, API questions, or anything
   where the reference files don't have enough detail, search or fetch from QuPath's official
   documentation:
   - Main docs: `https://qupath.readthedocs.io/en/stable/`
   - Javadoc API: `https://qupath.github.io/javadoc/docs/`
   - Community forum: `https://forum.image.sc/tag/qupath`
   - GitHub: `https://github.com/qupath/qupath`

4. **Provide actionable answers.** Don't just explain — give the user something they can immediately
   use: a menu path, a script snippet, a setting to change, or a step-by-step workflow.

## Key Principles

- **QuPath version awareness**: The latest stable release is QuPath 0.6.0. When the user's version
  matters (and it often does for scripting), ask or check. Many scripts from 0.4.x need adjustments
  for 0.5.x+ and 0.6.x.

- **Run vs Run for Project**: This distinction trips up many users. "Run" executes on the current
  image without saving. "Run for Project" saves to the data file, not to the currently viewed image.
  Mention this whenever sharing scripts that modify data.

- **Include default imports**: Always remind users to check that `Run → Include default imports` is
  enabled in the Script Editor. Without it, scripts will fail with class-not-found errors.

- **Project-based workflows**: Encourage project-based organization. Many features (batch processing,
  classifiers, measurements export) only work properly within a project context.

- **Error messages matter**: QuPath errors often appear in the log (`View → Show log`). When
  troubleshooting, always ask the user to check the log for the full error.

## QuPath Architecture Quick Reference

Understanding QuPath's object model helps with both UI use and scripting:

- **Hierarchy**: Root → Annotations → Detections (cells, tiles) → Sub-detections
- **PathObject**: Base class for all objects. Has a ROI, classification, and measurements.
- **ImageData**: Contains the image, hierarchy, and metadata for a single image.
- **Project**: Collection of image entries with shared classifiers and scripts.
- **Key classes for scripting**: `QP` (static methods), `PathObjects` (create objects),
  `ROIs` (create regions), `GsonTools` (JSON I/O), `GeometryTools` (spatial operations)

## Reference Files

Read the appropriate reference file(s) based on the user's question:

| File | When to read |
|------|-------------|
| `references/troubleshooting.md` | Error messages, unexpected behavior, performance issues, installation problems |
| `references/ui-guide.md` | Interface navigation, tools, panels, keyboard shortcuts, preferences |
| `references/analysis-workflows.md` | Cell detection, tissue classification, pixel classification, TMA, multiplexed imaging |
| `references/scripting-guide.md` | Groovy scripts, batch processing, custom measurements, data export, automation |

## Examples

**User says**: "My script worked on one image but Run for Project does nothing."
**Actions**: Recognize troubleshooting category → read `troubleshooting.md` ("Script runs but
nothing happens") → explain that Run for Project saves to disk, not the live view; suggest
`File → Reload data` and checking the log.

**User says**: "I'm new to QuPath, how do I annotate tumor regions on H&E?"
**Actions**: Beginner UI question → read `ui-guide.md` (drawing tools) → first remind them to set
image type (Brightfield H&E), then walk through Brush/Wand/Polygon tools and the Set class step.

**User says**: "How do I score Ki-67 and get a positive percentage?"
**Actions**: Analysis workflow → read `analysis-workflows.md` (H-DAB / IHC section) → give the
6-step workflow (set H-DAB type, annotate hot-spot, cell detection, intensity classification,
read counts) plus the positive-percentage Groovy snippet.

**User says**: "Export all cell measurements from every image to one CSV."
**Actions**: Scripting → read `scripting-guide.md` → offer the built-in `Measure → Export
measurements` first, then the project-wide iteration script for full control.

**User says**: "What changed in the QuPath scripting API in 0.6?"
**Actions**: Version-specific → check `scripting-guide.md` (Version Compatibility Notes), then
fetch the official docs/javadoc if more detail is needed.
