# QuPath Groovy Scripting Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Core Concepts](#core-concepts)
3. [Common Script Patterns](#common-script-patterns)
4. [Working with Objects](#working-with-objects)
5. [Creating & Modifying ROIs](#creating--modifying-rois)
6. [Measurements](#measurements)
7. [Data Export](#data-export)
8. [Data Import](#data-import)
9. [Image Access & Pixel Data](#image-access--pixel-data)
10. [Batch Processing Patterns](#batch-processing-patterns)
11. [Extension Development](#extension-development)

---

## Getting Started

### Script Editor
Open via `Automate → Show script editor`. Key things to check:
- `Run → Include default imports` — **always keep this ON**. It imports `QP`, `QPEx`, and
  other essential classes.
- `Run` (Ctrl+R) — runs on current image, does NOT save
- `Run for Project` (Ctrl+Shift+R) — runs on all/selected project images, SAVES results

### Default Imports
When "Include default imports" is enabled, you have access to:
```groovy
import static qupath.lib.gui.scripting.QPEx.*
// Which gives you all static methods from QP and QPEx, including:
// getAnnotationObjects(), getDetectionObjects(), getCurrentImageData(),
// addObject(), removeObjects(), fireHierarchyUpdate(), etc.
```

### Hello World
```groovy
println "QuPath version: " + GeneralTools.getVersion()
println "Image: " + getCurrentImageData().getServer().getMetadata().getName()
println "Annotations: " + getAnnotationObjects().size()
println "Detections: " + getDetectionObjects().size()
```

### Version Compatibility Notes
Scripts from older QuPath versions may need adjustments:

| Change | Old (0.4.x) | New (0.5.x / 0.6.x) |
|--------|-------------|---------------------|
| Get image name | `getProjectEntry().getImageName()` | `getCurrentServer().getMetadata().getName()` |
| Pixel size | `server.getPixelWidthMicrons()` | `server.getPixelCalibration().getPixelWidthMicrons()` |
| Remove measurements | `removeMeasurements(...)` | `removeDetectionMeasurements(...)` or `removeAnnotationMeasurements(...)` |
| ImageJ integration | Built-in macro runner | Extensions → ImageJ → ImageJ script runner (0.6.0) |
| Object IDs | Not reliably available | `object.getID()` (stable UUIDs) |

When adapting scripts found online, always check which QuPath version they target. The
community forum at image.sc often has updated versions in the replies.

---

## Core Concepts

### The Object Hierarchy
Everything in QuPath is organized in a hierarchy:
```
Root object
├── Annotation 1 ("Tumor")
│   ├── Detection (cell) 1
│   ├── Detection (cell) 2
│   └── ...
├── Annotation 2 ("Stroma")
│   └── ...
└── TMA Core (if applicable)
    └── ...
```

Access the hierarchy:
```groovy
def hierarchy = getCurrentHierarchy()
def root = hierarchy.getRootObject()
```

### PathObjects
Every annotation, detection, cell, and TMA core is a `PathObject`. Key properties:
- `.getROI()` — the region of interest (shape/geometry)
- `.getPathClass()` — the classification (e.g., "Tumor", "Positive")
- `.getMeasurements()` — numerical measurements
- `.getParent()` / `.getChildObjects()` — hierarchy relationships
- `.isAnnotation()` / `.isDetection()` — type checks

### Classifications (PathClass)
```groovy
// Get or create a classification
def tumorClass = getPathClass("Tumor")
def positiveClass = getPathClass("Positive")
def derived = getDerivedPathClass(tumorClass, "Positive")  // "Tumor: Positive"

// Set classification
object.setPathClass(tumorClass)
```

---

## Common Script Patterns

### Get Objects by Type and Class
```groovy
// All annotations
def annotations = getAnnotationObjects()

// All detections (includes cells)
def detections = getDetectionObjects()

// Only cells
def cells = getCellObjects()

// Filter by class
def tumorCells = getDetectionObjects().findAll {
    it.getPathClass() == getPathClass("Tumor")
}

// Filter by measurement
def largeCells = getCellObjects().findAll {
    it.getMeasurements().get("Nucleus: Area µm^2") > 50
}
```

### Select Objects
```groovy
// Select all annotations
selectAnnotations()

// Select specific objects
def objects = getAnnotationObjects().findAll { it.getPathClass() == getPathClass("Tumor") }
getCurrentHierarchy().getSelectionModel().setSelectedObjects(objects, null)
```

### Remove Objects
```groovy
// Remove all detections
removeObjects(getDetectionObjects(), true)

// Remove specific objects
def toRemove = getAnnotationObjects().findAll { it.getPathClass() == getPathClass("Other") }
removeObjects(toRemove, true)
```

### Rename/Reclassify
```groovy
// Change class of selected objects
def selected = getSelectedObjects()
selected.each { it.setPathClass(getPathClass("NewClass")) }
fireHierarchyUpdate()

// Change class based on measurement
getCellObjects().each { cell ->
    def dab = cell.getMeasurements().get("DAB: Mean")
    if (dab > 0.2)
        cell.setPathClass(getPathClass("Positive"))
    else
        cell.setPathClass(getPathClass("Negative"))
}
fireHierarchyUpdate()
```

---

## Working with Objects

### Create Annotations Programmatically
```groovy
import qupath.lib.objects.PathObjects
import qupath.lib.roi.ROIs
import qupath.lib.regions.ImagePlane

def plane = ImagePlane.getDefaultPlane()

// Rectangle annotation
def roi = ROIs.createRectangleROI(100, 200, 500, 300, plane)
def annotation = PathObjects.createAnnotationObject(roi, getPathClass("Region"))
addObject(annotation)

// Ellipse annotation
def ellipseRoi = ROIs.createEllipseROI(100, 200, 500, 300, plane)
addObject(PathObjects.createAnnotationObject(ellipseRoi))

// Point annotation
def pointRoi = ROIs.createPointsROI([100, 200, 300] as double[], [150, 250, 350] as double[], plane)
addObject(PathObjects.createAnnotationObject(pointRoi, getPathClass("Points")))
```

### Create Detections
```groovy
def plane = ImagePlane.getDefaultPlane()
def roi = ROIs.createEllipseROI(x, y, width, height, plane)
def detection = PathObjects.createDetectionObject(roi, getPathClass("Positive"))
addObject(detection)
```

### Merge/Split Annotations
```groovy
// Merge selected annotations
def selected = getSelectedObjects().findAll { it.isAnnotation() }
if (selected.size() > 1) {
    def rois = selected.collect { it.getROI() }
    def merged = RoiTools.union(rois)
    def newAnnotation = PathObjects.createAnnotationObject(merged, selected[0].getPathClass())
    removeObjects(selected, true)
    addObject(newAnnotation)
}
```

### Resolve Hierarchy (assign detections to annotations)
```groovy
resolveHierarchy()
```

---

## Creating & Modifying ROIs

### Geometry Operations
QuPath ROIs wrap JTS (Java Topology Suite) geometries, enabling powerful spatial operations:
```groovy
import qupath.lib.roi.GeometryTools

def anno1 = getAnnotationObjects()[0]
def anno2 = getAnnotationObjects()[1]

// Convert ROI to JTS geometry
def geom1 = anno1.getROI().getGeometry()
def geom2 = anno2.getROI().getGeometry()

// Spatial operations
def union = geom1.union(geom2)
def intersection = geom1.intersection(geom2)
def difference = geom1.difference(geom2)
def buffer = geom1.buffer(50)  // expand by 50 pixels

// Convert back to ROI
def plane = anno1.getROI().getImagePlane()
def newRoi = GeometryTools.geometryToROI(union, plane)
addObject(PathObjects.createAnnotationObject(newRoi, getPathClass("Merged")))
```

### Scale and Transform
```groovy
import org.locationtech.jts.geom.util.AffineTransformation

def roi = getSelectedObject().getROI()
def geom = roi.getGeometry()

// Scale by 2x from centroid
def centroid = geom.getCentroid()
def transform = AffineTransformation.scaleInstance(2, 2, centroid.getX(), centroid.getY())
def scaled = transform.transform(geom)

def newRoi = GeometryTools.geometryToROI(scaled, roi.getImagePlane())
addObject(PathObjects.createAnnotationObject(newRoi))
```

---

## Measurements

### Access Measurements
```groovy
def cell = getCellObjects()[0]
def measurements = cell.getMeasurements()

// Get specific measurement
def area = measurements.get("Nucleus: Area µm^2")
println "Nucleus area: ${area}"

// List all available measurements
measurements.keySet().each { println it }
```

### Add Custom Measurements
```groovy
def cells = getCellObjects()
cells.each { cell ->
    def nucleusArea = cell.getMeasurements().get("Nucleus: Area µm^2")
    def cellArea = cell.getMeasurements().get("Cell: Area µm^2")
    if (nucleusArea != null && cellArea != null && cellArea > 0) {
        def ncRatio = nucleusArea / cellArea
        cell.getMeasurements().put("NC Ratio", ncRatio)
    }
}
fireHierarchyUpdate()
```

### Add Shape Measurements
```groovy
// Add shape features (area, perimeter, circularity, etc.) to detections
def server = getCurrentServer()
def detections = getDetectionObjects()
ObjectMeasurements.addShapeMeasurements(
    detections,
    server,
    ObjectMeasurements.ShapeFeatures.values()
)
fireHierarchyUpdate()
```

---

## Data Export

### Export Measurements to CSV
```groovy
// Quick export via menu: Measure → Export measurements

// Script-based export:
def path = buildFilePath(PROJECT_BASE_DIR, "results", "measurements.csv")
new File(path).parentFile.mkdirs()

def sb = new StringBuilder()
sb.append("Image\tClass\tArea\tPerimeter\n")

for (detection in getDetectionObjects()) {
    def name = getCurrentImageData().getServer().getMetadata().getName()
    def cls = detection.getPathClass()?.toString() ?: "Unclassified"
    def area = detection.getMeasurements().get("Area µm^2") ?: ""
    def perim = detection.getMeasurements().get("Perimeter µm") ?: ""
    sb.append("${name}\t${cls}\t${area}\t${perim}\n")
}
new File(path).text = sb.toString()
println "Exported to: ${path}"
```

### Export Annotations as GeoJSON
```groovy
def annotations = getAnnotationObjects()
def gson = GsonTools.getInstance(true)  // true = include measurements
def path = buildFilePath(PROJECT_BASE_DIR, "export", "annotations.geojson")
new File(path).parentFile.mkdirs()
new File(path).text = gson.toJson(annotations)
println "Exported ${annotations.size()} annotations to: ${path}"
```

### Export Detections as GeoJSON
```groovy
def detections = getDetectionObjects()
def gson = GsonTools.getInstance(true)
def path = buildFilePath(PROJECT_BASE_DIR, "export", "detections.geojson")
new File(path).parentFile.mkdirs()
new File(path).text = gson.toJson(detections)
println "Exported ${detections.size()} detections to: ${path}"
```

### Export Image Regions
```groovy
// Export a region around each annotation as a TIFF
import qupath.lib.images.writers.ome.OMEPyramidWriter

def server = getCurrentServer()
def annotations = getAnnotationObjects()

annotations.eachWithIndex { anno, idx ->
    def roi = anno.getROI()
    def request = RegionRequest.createInstance(
        server.getPath(), 1.0, // downsample
        roi.getBoundsX() as int, roi.getBoundsY() as int,
        roi.getBoundsWidth() as int, roi.getBoundsHeight() as int
    )
    def img = server.readRegion(request)
    def path = buildFilePath(PROJECT_BASE_DIR, "export", "region_${idx}.tif")
    new File(path).parentFile.mkdirs()
    ImageIO.write(img, "TIFF", new File(path))
}
```

---

## Data Import

### Import Annotations from GeoJSON
```groovy
def path = "/path/to/annotations.geojson"
def json = new File(path).text
def gson = GsonTools.getInstance()
def type = new com.google.gson.reflect.TypeToken<List<qupath.lib.objects.PathObject>>(){}.getType()
def objects = gson.fromJson(json, type)
addObjects(objects)
println "Imported ${objects.size()} objects"
```

### Import Annotations from ImageJ ROIs
```groovy
// Drag and drop .roi or .zip files from ImageJ onto the QuPath viewer
// Or use the Extensions → ImageJ menu for more control
```

---

## Image Access & Pixel Data

### Read Pixel Data
```groovy
def server = getCurrentServer()
def roi = getSelectedObject().getROI()

// Read a region
def request = RegionRequest.createInstance(
    server.getPath(),
    1.0,  // downsample (1.0 = full resolution)
    roi.getBoundsX() as int,
    roi.getBoundsY() as int,
    roi.getBoundsWidth() as int,
    roi.getBoundsHeight() as int
)
def img = server.readRegion(request)
println "Image size: ${img.getWidth()} x ${img.getHeight()}"
```

### Get Image Metadata
```groovy
def server = getCurrentServer()
def metadata = server.getMetadata()

println "Image name: ${metadata.getName()}"
println "Width: ${server.getWidth()}"
println "Height: ${server.getHeight()}"
println "Pixel size: ${metadata.getPixelCalibration().getPixelWidthMicrons()} µm"
println "Channels: ${server.nChannels()}"
println "Image type: ${getCurrentImageData().getImageType()}"
```

---

## Batch Processing Patterns

### Built-in Export (no scripting needed)
For most measurement export needs, use `Measure → Export measurements` from the menu.
It exports all detection measurements across the entire project to a single file.

### Run Script Across Project (Run for Project)
Use this when each image needs the same processing independently:
```groovy
// This pattern works with "Run for Project":
def imageData = getCurrentImageData()
def server = imageData.getServer()
def imageName = server.getMetadata().getName()

println "Processing: ${imageName}"

// Your analysis steps here...
def annotations = getAnnotationObjects()
if (annotations.isEmpty()) {
    println "  No annotations found, skipping"
    return
}

// Run detection, classification, etc.
// Results are automatically saved when using "Run for Project"

println "  Done - found ${getDetectionObjects().size()} detections"
```

### Project-wide Iteration (Programmatic)
Use this when you need to aggregate data across images into a single output.
Run with **Run** (Ctrl+R), NOT "Run for Project" — the script handles iteration itself:
```groovy
// Export all cell measurements across the entire project to one CSV
def project = getProject()
if (project == null) {
    println "ERROR: No project open!"
    return
}

def outputPath = buildFilePath(PROJECT_BASE_DIR, "results", "all_measurements.csv")
new File(outputPath).parentFile.mkdirs()

// First pass: collect all measurement names across images
def allMeasurementNames = new LinkedHashSet<String>()
def imageEntries = project.getImageList()

println "Scanning ${imageEntries.size()} images for measurement names..."
for (entry in imageEntries) {
    def imageData = entry.readImageData()
    for (det in imageData.getHierarchy().getDetectionObjects()) {
        allMeasurementNames.addAll(det.getMeasurements().keySet())
    }
    imageData.close()
}

// Second pass: write CSV with consistent columns
def sep = ","
def sb = new StringBuilder()
sb.append("Image${sep}Object ID${sep}Class")
for (name in allMeasurementNames) sb.append("${sep}${name}")
sb.append("\n")

for (entry in imageEntries) {
    def imageData = entry.readImageData()
    def imageName = entry.getImageName()
    for (det in imageData.getHierarchy().getDetectionObjects()) {
        sb.append("${imageName}${sep}${det.getID()}${sep}")
        sb.append("${det.getPathClass()?.toString() ?: 'Unclassified'}")
        for (name in allMeasurementNames) {
            def val = det.getMeasurements().get(name)
            sb.append("${sep}${val != null ? val : ''}")
        }
        sb.append("\n")
    }
    imageData.close()
    println "  Exported from: ${imageName}"
}

new File(outputPath).text = sb.toString()
println "Done! Saved to: ${outputPath}"
```

**Key difference**: "Run for Project" processes images independently and saves each one.
Programmatic iteration with `project.getImageList()` lets you read all images and write
a combined output. Always call `imageData.close()` after each image to free memory.

### Project-wide Summary
```groovy
// Run this with "Run for Project" to collect summary stats
def imageName = getCurrentServer().getMetadata().getName()
def nAnnotations = getAnnotationObjects().size()
def nDetections = getDetectionObjects().size()
def nPositive = getDetectionObjects().count { it.getPathClass() == getPathClass("Positive") }

println "${imageName}\t${nAnnotations}\t${nDetections}\t${nPositive}"
```

---

## Quick Recipes

Copy-paste-ready scripts for the most common tasks.

### Calculate positive cell percentage
```groovy
def detections = getDetectionObjects()
def positive = detections.count { it.getPathClass() == getPathClass("Positive") }
def negative = detections.count { it.getPathClass() == getPathClass("Negative") }
def total = positive + negative
println "Positive: ${positive}/${total} (${total > 0 ? (positive/total*100).round(1) : 0}%)"
```

### Count cells per annotation
```groovy
for (anno in getAnnotationObjects()) {
    def children = anno.getChildObjects().findAll { it.isDetection() }
    def className = anno.getPathClass()?.toString() ?: "Unclassified"
    println "${className}: ${children.size()} cells"
}
```

### Export annotation areas to CSV
```groovy
def sb = new StringBuilder("Class,Area µm²,Perimeter µm\n")
for (anno in getAnnotationObjects()) {
    def cls = anno.getPathClass()?.toString() ?: "Unclassified"
    def area = anno.getROI().getArea()  // in pixels²
    def cal = getCurrentServer().getPixelCalibration()
    def areaUm = area * cal.getPixelWidthMicrons() * cal.getPixelHeightMicrons()
    sb.append("${cls},${areaUm.round(1)}\n")
}
def path = buildFilePath(PROJECT_BASE_DIR, "results", "annotation_areas.csv")
new File(path).parentFile.mkdirs()
new File(path).text = sb.toString()
println "Saved to: ${path}"
```

### Batch rename classifications
```groovy
// Rename "Old Class" to "New Class" for all detections
def oldName = "Old Class"
def newName = "New Class"
def newClass = getPathClass(newName)
def changed = 0
getDetectionObjects().each {
    if (it.getPathClass()?.toString() == oldName) {
        it.setPathClass(newClass)
        changed++
    }
}
fireHierarchyUpdate()
println "Renamed ${changed} objects from '${oldName}' to '${newName}'"
```

### Delete all detections outside annotations
```groovy
def toRemove = getDetectionObjects().findAll { it.getParent() == null || it.getParent().isRootObject() }
removeObjects(toRemove, true)
println "Removed ${toRemove.size()} orphan detections"
```

### Set pixel size (when metadata is missing)
```groovy
// Set pixel size to 0.25 µm (adjust to your scanner's calibration)
setPixelSizeMicrons(0.25, 0.25)
println "Pixel size set to 0.25 µm"
```

---

## Extension Development

For developers building QuPath extensions:

### Extension Structure
QuPath extensions implement `QuPathExtension` interface:
```groovy
import qupath.lib.gui.extensions.QuPathExtension

class MyExtension implements QuPathExtension {
    @Override
    String getName() { return "My Extension" }

    @Override
    String getDescription() { return "Does something useful" }

    @Override
    void installExtension(QuPathGUI qupath) {
        // Add menu items, tools, etc.
    }
}
```

### Key Resources for Developers
- QuPath Javadoc: `https://qupath.github.io/javadoc/docs/`
- GitHub source: `https://github.com/qupath/qupath`
- Extension examples: `https://github.com/qupath/qupath-extension-template`
- Build system: Gradle with Java 17+
- The `image.sc` forum is the best place for development questions

### Using IntelliJ for Scripting
For serious script development, use IntelliJ IDEA with Groovy support:
1. Set up a Gradle project referencing QuPath JARs
2. Point the script directory in QuPath to your project's script folder
3. Enable `File → Auto refresh files` in QuPath's Script Editor
4. Edit in IntelliJ (with autocomplete), run in QuPath
