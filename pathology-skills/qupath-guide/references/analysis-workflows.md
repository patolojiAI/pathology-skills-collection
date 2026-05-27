# QuPath Analysis Workflows

## Table of Contents
1. [General Workflow Pattern](#general-workflow-pattern)
2. [Cell Detection (Brightfield)](#cell-detection-brightfield)
3. [Cell Detection (Fluorescence)](#cell-detection-fluorescence)
4. [Tissue Detection & Annotation](#tissue-detection--annotation)
5. [Pixel Classification](#pixel-classification)
6. [Object Classification](#object-classification)
7. [TMA Analysis](#tma-analysis)
8. [Multiplex / Multi-channel Analysis](#multiplex--multi-channel-analysis)
9. [Stain Vectors & Deconvolution](#stain-vectors--deconvolution)
10. [Batch Processing](#batch-processing)

---

## General Workflow Pattern

Most QuPath analyses follow this sequence:

1. **Set image type** → `Image → Set image type` (H&E, H-DAB, Fluorescence, etc.)
2. **Create annotations** → Define regions of interest (tumor, stroma, etc.)
3. **Run detection** → Find cells/objects within annotations
4. **Classify** → Assign classes to detected objects (positive/negative, cell types)
5. **Measure** → Extract measurements from objects
6. **Export** → Save results as CSV, GeoJSON, or images

Skipping step 1 is a common source of errors — many analysis tools behave differently
depending on the image type.

---

## Cell Detection (Brightfield)

### Standard H&E Cell Detection

1. Set image type: `Image → Set image type → Brightfield (H&E)`
2. Draw annotation(s) around region(s) of interest
3. Select the annotation(s)
4. Run: `Analyze → Cell detection`

**Key parameters:**
- **Requested pixel size (µm)**: Controls analysis resolution. 0.5 µm is a good default for
  most applications. Lower = more accurate but slower.
- **Background radius (µm)**: Helps with uneven illumination. Typically 8-15 µm.
- **Median filter radius**: Noise reduction. Usually 0-1.
- **Sigma (µm)**: Gaussian smoothing for nucleus detection. Typically 1.5-3.
- **Minimum/Maximum area (µm²)**: Filter out too-small (debris) or too-large (clumps) detections.
- **Threshold**: Detection sensitivity. Lower = more detections. Adjust based on staining
  intensity.
- **Cell expansion (µm)**: How far to expand from nucleus to estimate cytoplasm. Typically 3-5 µm.

### H-DAB (Immunohistochemistry)

IHC scoring is one of the most common QuPath tasks. The general workflow:

1. **Set image type**: `Image → Set image type → Brightfield (H-DAB)`. This tells QuPath
   the slide uses hematoxylin + DAB staining, enabling proper color deconvolution.
2. **Check stain vectors**: `Analyze → Preprocessing → Estimate stain vectors`. If colors
   look off after setting image type, re-estimate on a representative region.
3. **Annotate regions of interest**: Draw around the area to score. For Ki-67 and similar
   proliferation markers, annotate the "hot spot" — the area with the highest density of
   positive cells. Scan the slide at low magnification first to identify it.
4. **Run cell detection**: Select annotation(s) → `Analyze → Cell detection`. For IHC:
   - Requested pixel size: 0.5 µm
   - Cell expansion: 2-3 µm (most IHC markers are nuclear, so keep this small)
   - Adjust threshold based on the hematoxylin (blue) channel for nuclear detection
5. **Classify by intensity**: `Classify → Object classification → Set cell intensity classifications`
   - Select the **DAB: Mean** measurement as the scoring channel
   - Set threshold(s) to separate Negative from Positive (or 1+/2+/3+ for graded scoring)
   - Preview the classification and adjust until it matches visual assessment
6. **Read results**: Select your annotation — the Annotations panel shows detection counts
   per class. The positive percentage is: Positive / (Positive + Negative) × 100%.

**Quick positive percentage script:**
```groovy
def detections = getDetectionObjects()
def positive = detections.count { it.getPathClass() == getPathClass("Positive") }
def negative = detections.count { it.getPathClass() == getPathClass("Negative") }
def total = positive + negative
def percentage = total > 0 ? (positive / total * 100).round(1) : 0
println "Positive: ${positive}/${total} (${percentage}%)"
```

**Common IHC markers and image types:**

| Marker | Image Type | Scoring Method |
|--------|-----------|----------------|
| Ki-67, p53, ER, PR | H-DAB | Nuclear intensity → Positive/Negative |
| HER2 (IHC) | H-DAB | Membrane intensity → 0/1+/2+/3+ |
| CD3, CD8, CD20 | H-DAB | Cell count per area (density) |
| PD-L1 | H-DAB | Combined proportion score or tumor proportion score |
| Dual stains (e.g., CD8/PD-L1) | Brightfield (Other) | Custom stain vectors needed |

**Hot-spot analysis tip**: For proliferation markers like Ki-67, the hot-spot matters more
than whole-slide average. Draw a small annotation (~1-2 mm²) in the most proliferative area.
Some protocols require evaluating multiple hot spots and reporting the highest value.

---

## Cell Detection (Fluorescence)

1. Set image type: `Image → Set image type → Fluorescence`
2. Identify which channel contains nuclear signal (typically DAPI)
3. Draw annotation(s)
4. Run: `Analyze → Cell detection`
   - Set **Detection channel** to your nuclear marker (e.g., DAPI)
   - Adjust threshold for fluorescence intensity
   - Cell expansion captures signal from other channels

**Tip**: For fluorescence, you often want to classify cells based on intensity thresholds
in multiple channels. Use `Classify → Object classification → Set cell intensity classifications`
with appropriate channel-specific thresholds.

---

## Tissue Detection & Annotation

### Automatic Tissue Detection
- `Analyze → Preprocessing → Simple tissue detection` creates an annotation around the
  tissue area, excluding background.
- Useful as a first step before running cell detection across the entire tissue.

### Thresholding for Annotation
- `Classify → Pixel classification → Create thresholder` allows creating annotations based
  on pixel intensity thresholds. Good for separating tissue from background or identifying
  stained regions.

### Annotation Transfer
To copy annotations between images in a project, use a script:
```groovy
// In the source image, export annotations:
def annotations = getAnnotationObjects()
def gson = GsonTools.getInstance(true)
println gson.toJson(annotations)

// In the target image, import (paste the JSON):
def gson = GsonTools.getInstance(true)
def json = '...'  // paste JSON here
def type = new com.google.gson.reflect.TypeToken<List<qupath.lib.objects.PathObject>>(){}.getType()
def objects = gson.fromJson(json, type)
addObjects(objects)
```

---

## Pixel Classification

Pixel classifiers assign a class to every pixel in the image. Useful for area-based
measurements (e.g., % tumor vs stroma).

### Training a Pixel Classifier

1. Create annotation regions and assign classes (e.g., "Tumor", "Stroma", "Necrosis")
   using `Right-click → Set class`
2. Open: `Classify → Pixel classification → Train pixel classifier`
3. Configure:
   - **Resolution**: Lower resolution = faster, less detailed. Start with 10-20 µm/px for
     tissue-level classification, 1-5 µm/px for finer detail.
   - **Features**: Select image features (Gaussian, Laplacian, etc.) at relevant scales
   - **Classifier type**: Random Trees works well for most cases
4. Click **Train** — the classifier updates live as you add/modify training annotations
5. Save the classifier: `Save & Apply`

### Applying Pixel Classifier
- Results appear as an overlay. Toggle with `Shift+O`.
- To create measurement: select annotations → `Classify → Pixel classification → Add measurements`
- To create objects from classified regions: `Classify → Pixel classification → Create objects`

---

## Object Classification

Object classifiers assign a class to each detected object (cell, detection) based on
their measurements.

### Training an Object Classifier

1. First, run cell detection to create objects
2. Manually classify some representative objects (right-click → Set class)
3. Open: `Classify → Object classification → Train object classifier`
4. Select features to use (measurements from the detection step)
5. Train and apply

### Single Measurement Classifier
For simple cases like positive/negative IHC scoring:
- `Classify → Object classification → Create single measurement classifier`
- Choose the measurement (e.g., "DAB: Mean") and set threshold
- Objects above threshold get one class, below get another

---

## TMA Analysis

### TMA Dearraying
1. Open the TMA slide
2. `TMA → TMA dearrayer`
3. Adjust grid parameters:
   - Provide estimated core diameter
   - QuPath will attempt to detect and arrange cores automatically
   - Manually adjust misplaced cores by dragging
4. Label cores with identifiers as needed

### Per-Core Analysis
After dearraying, each core becomes its own annotation. Run detection and classification
within each core, then export results per core.

### TMA Results Viewer
- `TMA → Show TMA results` provides a grid view of all cores
- Color-code by any measurement for quick visual assessment
- Useful for identifying outliers and quality control

---

## Multiplex / Multi-channel Analysis

For multiplexed imaging (e.g., Vectra, CODEX, mIF):

1. Set image type to `Fluorescence`
2. Adjust channel display via `Brightness/Contrast` (toolbar icon)
3. Rename channels to marker names: script or `Image → Set channel names`
4. Cell detection using a nuclear channel (DAPI)
5. Classify cells based on multi-channel intensity thresholds

**Tip**: For complex multiplex panels, consider using a trained object classifier rather
than manual thresholding. Train on a few well-characterized examples for each phenotype.

---

## Stain Vectors & Deconvolution

Stain vectors define how QuPath separates color channels in brightfield images.

### Estimating Stain Vectors
1. `Analyze → Preprocessing → Estimate stain vectors`
2. Select a representative region containing both stains
3. QuPath estimates the vectors automatically
4. Fine-tune manually if the automatic estimate looks off

### Common Issues
- **Wrong image type**: Must be set to a brightfield type first
- **Background too dark/light**: The background (white) value matters. Adjust in stain
  vector editor if tissue appears washed out or too dark.
- **Inconsistent staining**: Stain vectors should ideally be estimated per-image or per-batch
  if staining varies significantly between slides.

---

## Exporting Results

### Built-in Measurement Export (recommended for most users)
The fastest way to get measurements out of QuPath:

- **Single image**: `Measure → Show detection measurements` → click "Save" to export as TSV
- **Whole project**: `Measure → Export measurements` → exports all detection measurements
  across every image in the project into a single file. Choose CSV or TSV format.

This built-in export handles column alignment automatically (even when different images have
different measurement sets) and is sufficient for most scoring and counting tasks.

Use scripting instead when you need: custom column selection, filtered subsets, special
formatting, or integration with external pipelines.

---

## Batch Processing

### Using Scripts for Batch Processing
1. Develop and test your script on a single image using "Run"
2. Once satisfied, use "Run for Project" to apply to all (or selected) images
3. Results are saved directly to each image's data file

### Workflow to Script
QuPath can convert UI actions to a script:
1. Perform your analysis steps manually on one image
2. `Automate → Show workflow` — this captures your steps
3. `Create script` to generate a Groovy script from the workflow
4. Review and edit the script as needed
5. Run for the entire project

This is one of QuPath's most powerful features — it bridges the gap between interactive
use and batch automation.
