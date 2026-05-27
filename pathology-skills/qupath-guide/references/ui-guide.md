# QuPath UI & Navigation Guide

## Table of Contents
1. [Main Window Layout](#main-window-layout)
2. [Toolbar & Drawing Tools](#toolbar--drawing-tools)
3. [Panels & Views](#panels--views)
4. [Keyboard Shortcuts](#keyboard-shortcuts)
5. [Preferences & Configuration](#preferences--configuration)
6. [Project Management](#project-management)

---

## Before You Start — Essential First Steps

Before doing anything with a new image, set these up:

1. **Set the image type**: `Image → Set image type`. Choose the correct type for your staining:
   - **Brightfield (H&E)** — standard histology
   - **Brightfield (H-DAB)** — immunohistochemistry (brown DAB + blue hematoxylin)
   - **Brightfield (Other)** — other chromogenic stains (set stain vectors manually)
   - **Fluorescence** — DAPI, FITC, Cy3, multiplexed imaging, etc.

   Getting this wrong causes incorrect stain separation, wrong measurements, and confusing
   detection results. When in doubt, set it to H&E for routine histology.

2. **Verify pixel calibration**: Check `Image → Image details` to confirm pixel size is set
   correctly. If it shows "Unknown" or wrong values, all area/length measurements will be off.
   Fix it with: `setPixelSizeMicrons(0.25, 0.25)` in the Script Editor (adjust to your scanner).

3. **Work within a project**: Create a project (`Project → Create project`) before starting
   serious analysis. Batch processing, classifiers, and measurement export all depend on it.

---

## Main Window Layout

QuPath's interface has these main areas:

- **Viewer (center)**: The main image canvas. Supports zoom (scroll wheel), pan (click-drag),
  and rotation. Multiple viewers can be opened side-by-side via `View → Multi-view`.
- **Toolbar (top)**: Drawing tools, zoom controls, and view toggles.
- **Tab panels (left/right)**: Configurable panels for project navigation, annotations,
  measurements, and more.
- **Status bar (bottom)**: Shows cursor position, pixel values, and current tool info.

### Navigation Basics
- **Zoom**: Scroll wheel, or use the zoom slider in the toolbar.
- **Pan**: Click and drag with the Move tool (shortcut: M), or hold spacebar while using
  another tool.
- **Fit to window**: Double-click the image thumbnail in the Overview panel.
- **Overview panel**: Shows a minimap of the entire slide. Click to jump to a location.

---

## Toolbar & Drawing Tools

### Tool Shortcuts

| Tool | Shortcut | Purpose |
|------|----------|---------|
| Move | M | Pan around the image |
| Rectangle | R | Draw rectangular annotations |
| Ellipse | O | Draw elliptical annotations |
| Polygon | P | Draw polygon annotations (click vertices, double-click to close) |
| Polyline | V | Draw line annotations |
| Brush | B | Paint freehand annotations |
| Wand | W | "Magic wand" — auto-detect regions by similarity |
| Points | . | Place point annotations |
| Selection | S | Select existing objects |

### Drawing Tips
- **Brush size**: Use `[` and `]` to decrease/increase brush size.
- **Eraser mode**: Hold `Alt` while using the Brush tool to erase.
- **Subtract from annotation**: Hold `Alt` while drawing with any shape tool to subtract
  from the selected annotation.
- **Add to annotation**: Hold `Shift` while drawing to merge with the selected annotation.
- **Lock annotations**: Right-click → Lock to prevent accidental modification.

### Wand Tool
The Wand tool is powerful for semi-automated annotation. Adjust sensitivity via
`Edit → Preferences → Drawing tools → Wand sensitivity`. Lower values = more strict matching.
It works with both brightfield and fluorescence images.

---

## Panels & Views

### Key Panels (toggle via View menu)

- **Project** (`View → Show project`): Lists all images in the current project. Double-click
  to open an image. Right-click for image metadata and options.
- **Annotations** (`View → Show annotations`): Lists all annotation objects. Click to select
  and center on an annotation. Manage classifications here.
- **Hierarchy** (`View → Show hierarchy`): Shows the full object tree. Useful for understanding
  parent-child relationships between annotations and detections.
- **Measurement table**: Shows measurements for selected objects. Can be sorted and filtered.
  Access via `Measure → Show detection/annotation measurements`. Click "Save" to export the
  current table. For project-wide export, use `Measure → Export measurements` — this writes
  all detection measurements across every image to a single file.
- **Log** (`View → Show log`): Critical for troubleshooting. Shows all system messages, errors,
  and script output.
- **Script Editor** (`Automate → Show script editor`): Write and run Groovy scripts.
- **Command list** (`Ctrl/Cmd + L`): Searchable list of all QuPath commands. Type to filter —
  fastest way to find any feature.

### Viewer Overlays
- **C**: Toggle cell display on/off
- **F**: Toggle fill for objects (filled vs outline only)
- **G**: Toggle grid overlay
- **Shift + C**: Cycle through classification colors
- **H**: Toggle annotation names display

### Brightness & Contrast
- Access via the icon in the toolbar or `View → Brightness/Contrast`.
- For brightfield: adjusts display of deconvolved stain channels.
- For fluorescence: controls per-channel display range and color.
- Changes are display-only — they don't modify the underlying image data.

---

## Keyboard Shortcuts

### Essential Shortcuts

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Command list | Ctrl+L | Cmd+L |
| Save | Ctrl+S | Cmd+S |
| Undo | Ctrl+Z | Cmd+Z |
| Redo | Ctrl+Shift+Z | Cmd+Shift+Z |
| Delete selected | Delete | Backspace |
| Select all annotations | Ctrl+A | Cmd+A |
| Run script | Ctrl+R | Cmd+R |
| Zoom to fit | Ctrl+Shift+F | Cmd+Shift+F |
| Toggle detections | D | D |
| Toggle annotations | A | A |
| Toggle TMA grid | T | T |
| Toggle pixel classification overlay | Shift+O | Shift+O |

### Script Editor Shortcuts

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Run script | Ctrl+R | Cmd+R |
| Run for project | Ctrl+Shift+R | Cmd+Shift+R |
| Comment/uncomment | Ctrl+/ | Cmd+/ |
| Find/Replace | Ctrl+F | Cmd+F |

---

## Preferences & Configuration

Access via `Edit → Preferences`. Key settings:

### General
- **Maximum memory**: Increase for large images or heavy analysis. Requires restart.
- **Number of threads**: Controls parallel processing. Default matches CPU core count.
- **Theme**: Light or Dark mode.

### Image Display
- **Interpolation**: Controls how pixels are displayed when zoomed in. Use "None" for
  pixel-perfect view at high zoom.
- **Background color**: Set the color shown outside the image bounds.

### Drawing Tools
- **Brush diameter**: Default brush size.
- **Wand sensitivity**: How aggressively the wand tool expands selection.
- **Use multipoint**: Whether the Points tool creates individual or grouped points.

### Extensions
- **Extensions directory**: Where QuPath looks for .jar extension files. Set this to a
  persistent directory.
- **Script directory**: Default location for shared scripts, accessible from the Script Editor.

---

## Project Management

### Creating a Project
1. `Project → Create project`
2. Choose an empty directory (QuPath will create subdirectories inside it)
3. Add images via `Project → Add images` or drag-and-drop

### Project Structure on Disk
```
my-project/
├── project.qpproj          # Project metadata (JSON)
├── data/
│   ├── image1/             # Per-image data
│   │   ├── data.qpdata     # Annotations, detections, metadata
│   │   └── ...
│   └── image2/
├── classifiers/            # Saved classifiers
│   ├── object_classifiers/
│   └── pixel_classifiers/
└── scripts/                # Project scripts (accessible from Automate menu)
```

### Image Management
- **Add images**: `Project → Add images` supports individual files, directories, and URIs.
- **Remove images**: Right-click in the Project panel → Remove.
- **Image metadata**: Right-click → Edit description to add notes. Right-click → Show image
  in Explorer/Finder to locate the source file.
- **Duplicate entries**: You can add the same image multiple times (e.g., for different
  analyses). Each entry maintains its own data independently.

### Sharing Projects
- The project directory is self-contained except for the original images.
- To share: include the project directory and ensure image paths are accessible on the
  target system. Update URIs if needed via `Project → Edit image URIs`.
