# QuPath Troubleshooting Guide

## Table of Contents
1. [Installation & Startup](#installation--startup)
2. [Image Loading Issues](#image-loading-issues)
3. [Memory & Performance](#memory--performance)
4. [Script Errors](#script-errors)
5. [Detection & Classification Issues](#detection--classification-issues)
6. [Export Problems](#export-problems)
7. [Project Corruption](#project-corruption)

---

## Installation & Startup

### QuPath won't launch
- **Java errors on startup**: QuPath bundles its own JDK; if launching from a custom setup, ensure
  Java 17+ is available. On macOS, you may need to right-click → Open on first launch due to
  Gatekeeper restrictions.
- **Blank/white screen**: May be a GPU driver issue. Try launching with `--opengl=software` flag
  from the command line.
- **"QuPath is damaged" (macOS)**: Run `xattr -cr /Applications/QuPath.app` in Terminal to clear
  the quarantine attribute.

### Extensions not loading
- Extensions (.jar files) go in the QuPath extensions directory. Find it via
  `Edit → Preferences → Extensions directory`. If the directory doesn't exist, create it.
- After adding extensions, restart QuPath.
- Check `View → Show log` for errors related to extension loading.

---

## Image Loading Issues

### "Could not open image" / unsupported format
- Check the file format. QuPath supports: SVS, NDPI, SCN, MRXS, TIFF, OME-TIFF, JPEG, PNG,
  and others via Bio-Formats and OpenSlide.
- For MRXS: all associated files (index files, data folder) must be present and co-located.
- For very large standard TIFFs: they may need to be pyramidal. Convert using bio-formats
  `bfconvert` or QuPath's built-in `convert-ome` command.

### Image appears blurry or wrong resolution
- QuPath may be reading a lower-resolution pyramid level. Check `Image → Image details` for
  pixel size information.
- If pixel size is missing or wrong: set it via a script or through `Automate → Show script editor`:
  ```groovy
  setPixelSizeMicrons(0.25, 0.25)
  ```

### Colors look wrong (stain separation)
- Go to `Image → Set image type` and confirm it's set correctly (e.g., Brightfield H&E,
  Brightfield H-DAB, Fluorescence).
- For brightfield: check stain vectors via `Analyze → Estimate stain vectors`. Poor stain
  vectors lead to bad deconvolution. You can manually adjust them.

---

## Memory & Performance

### OutOfMemoryError
- Increase memory allocation: `Edit → Preferences → General` and increase "Maximum memory".
  Restart QuPath after changing.
- Rule of thumb: allocate 50-75% of your system RAM to QuPath, but leave at least 4 GB for
  the OS.
- For very large analyses, consider processing tiles rather than the entire image at once.

### QuPath is very slow / freezing
- Check if detection objects are overwhelming the viewer. More than ~500,000 detections in a
  single image can slow things down significantly.
- Reduce tile cache if memory pressure is high.
- Close the measurement table if it's open during batch processing — it updates in real time
  and can cause slowdowns.
- On macOS: some users report better performance with Metal rendering disabled.

### Tile cache warnings
- The tile cache stores image tiles in memory for fast viewing. If it's too small, QuPath
  re-reads tiles constantly. Set it to 25-50% of max memory in Preferences.

---

## Script Errors

### "No such property" / "No such method"
- Most common cause: `Run → Include default imports` is not checked in the Script Editor.
  Enable it and retry.
- If still failing: the method may not exist in your QuPath version. Check the Javadoc for
  your version at `https://qupath.github.io/javadoc/docs/`.
- Common version-breaking changes:
  - 0.4.x → 0.5.x: Several `QPEx` methods moved or renamed
  - 0.5.x → 0.6.x: ImageJ integration redesigned, some script runner changes

### "Cannot resolve class" errors
- Missing import statement. If `Include default imports` is already on, you may need an explicit
  import for less common classes:
  ```groovy
  import qupath.lib.objects.PathObjects
  import qupath.lib.roi.ROIs
  import qupath.lib.regions.ImagePlane
  ```

### Script runs but nothing happens
- Check if you're using "Run" (doesn't save) vs "Run for Project" (saves to data file, not
  the current view). If you used "Run for Project" on the current image, reload via
  `File → Reload data`.
- Verify the script's output in the log (`View → Show log`).
- Make sure you call `fireHierarchyUpdate()` after modifying objects programmatically, so the
  viewer refreshes.

### Script works on one image but fails on others
- Image type may differ (brightfield vs fluorescence). Check with `getCurrentImageData().getImageType()`.
- Annotations or detections may be missing. Add guards:
  ```groovy
  def annotations = getAnnotationObjects()
  if (annotations.isEmpty()) {
      println "No annotations found - skipping"
      return
  }
  ```
- Pixel size may be undefined in some images, causing measurement calculations to fail.

---

## Detection & Classification Issues

### Cell detection finds too many / too few cells
- Adjust detection parameters systematically: start with the `Requested pixel size` (higher =
  faster but less precise), then tune `Threshold`, `Min/Max area`, and `Cell expansion`.
- For H&E: make sure stain vectors are correct — bad deconvolution leads to bad detection.
- Use `Analyze → Cell detection` preview mode to see detection results before committing.

### Pixel classifier gives unexpected results
- Check that the training annotations are correctly classified (right-click → Set class).
- Ensure sufficient and representative training regions. Include edge cases.
- Try different feature scales — the resolution at which features are computed matters a lot.
- Check the image type is set correctly before training.

### Objects have no measurements
- Measurements are computed during detection/classification. If you created objects via
  scripting, you may need to add measurements explicitly:
  ```groovy
  def server = getCurrentServer()
  def measurements = ObjectMeasurements.addShapeMeasurements(
      getDetectionObjects(), server, ObjectMeasurements.ShapeFeatures.values())
  ```

---

## Export Problems

### Measurements export is empty or incomplete
- **Using `Measure → Export measurements`?** This exports from saved data files. If you
  haven't saved (`Ctrl+S` or "Run for Project"), recent changes won't appear.
- **Using `Measure → Show detection measurements` → Save?** This exports only the current
  image's current view. Make sure objects are present and have measurements.
- Check that objects actually have measurements by selecting one and checking the
  Measurements panel. If measurements are empty, you may need to re-run detection or
  add measurements via script.

### Annotation/detection export to GeoJSON fails
- Very large numbers of objects can cause export to hang. Export in batches or use a script:
  ```groovy
  def annotations = getAnnotationObjects()
  def gson = GsonTools.getInstance(true)
  def file = new File(buildFilePath(PROJECT_BASE_DIR, "export", "annotations.geojson"))
  file.parentFile.mkdirs()
  file.text = gson.toJson(annotations)
  ```

### Image export looks different from viewer
- QuPath exports the raw image data, not the viewer display. If you want the display appearance
  (with overlays, stain separation colors, etc.), use `File → Export snapshot → Current viewer`.

---

## Project Corruption

### Project won't open / data files missing
- QuPath projects are stored as a `project.qpproj` file with associated data directories.
- If data files are corrupted, you can often recover by:
  1. Creating a new project
  2. Re-adding the images
  3. Copying any surviving `.qpdata` files from the old project's `data/` directory

### "Image not found" after moving files
- QuPath stores image paths. If you moved the original images, use
  `Project → Edit image URIs` (if available in your version) or manually edit the
  `project.qpproj` JSON file to update paths.

---

## Getting More Help

- **View → Show log**: Always check the log first. Copy the full error for sharing.
- **Forum**: Post questions at `https://forum.image.sc/tag/qupath` — include QuPath version,
  OS, image type, and the full error log.
- **GitHub Issues**: For confirmed bugs: `https://github.com/qupath/qupath/issues`
