# Lesson 02 – First Lung Segmentation

**Learning path:** 3D Slicer  
**Date:** Not recorded  
**Status:** Learning record  
**Scope:** Educational workflow; no clinical data or patient-specific conclusions

## Objectives

- Create a first educational lung segmentation with Segment Editor.
- Understand the roles of Threshold, Paint, and Grow from Seeds.
- Use Preview, Auto Update, and Apply as distinct stages of a semi-automatic workflow.
- Create separate segments for the right lung, left lung, body, and trachea.
- Inspect the segmentation in slice views and the 3D view.
- Use Segment Statistics to observe volume, voxel count, and mean Hounsfield unit values.
- Recognize that generated measurements require correct masks, geometry, and source-volume selection.

## Scientific Background

### Segment Editor and segments

Segment Editor is the 3D Slicer module used to create and modify labeled anatomical regions. A segmentation can contain multiple segments, with each segment representing a defined structure. Clear names and consistent colors help prevent editing the wrong region.

For this introductory workflow, the right lung, left lung, body, and trachea were treated as separate regions. Their separation supports individual visualization and statistics, but the anatomical boundary rules still need to be defined and reviewed.

### Threshold

Threshold selects voxels within an intensity range. In CT, voxel values are commonly expressed in Hounsfield units, which makes thresholding a useful starting point for distinguishing air-containing regions from denser tissues.

An intensity range does not understand anatomy. Air outside the patient, the lungs, trachea, and other low-density regions may overlap in value. Threshold therefore provides an initial candidate mask rather than a complete lung segmentation.

### Paint

Paint adds voxels to the active segment using a brush. It is useful for placing initial labels and correcting small missing areas. Brush size and slice orientation affect the edit, so corrections should be reviewed in adjacent slices and other planes.

### Grow from Seeds

Grow from Seeds uses labeled examples, or seeds, to estimate boundaries between regions. Representative seeds for the right lung, left lung, body, and trachea help the effect distinguish these regions using image information.

Seed placement is iterative. Incomplete or poorly positioned seeds can produce incorrect boundaries. The preview should be reviewed and seeds refined before the result is applied.

### Preview, Auto Update, and Apply

- **Preview** displays the proposed Grow from Seeds result without finalizing it.
- **Auto Update** refreshes the preview after seed edits when enabled.
- **Apply** accepts the preview and writes the calculated regions into the segments.

Apply should occur only after reviewing the preview in multiple slices. Applying is not equivalent to completing quality control.

### Segment Statistics

Segment Statistics calculates quantitative information from masks. Introductory outputs include:

- **Volume:** physical space occupied by the segment, derived from mask geometry.
- **Voxel count:** number of voxels included in the mask.
- **Mean HU:** average CT intensity inside the segment when the correct CT volume is selected as the scalar source.

These values depend on the segmentation boundary, source image, voxel spacing, and calculation settings. They are observations from the mask, not independent confirmation that the anatomy was segmented correctly.

## Practical Workflow

### 1. Confirm the CT volume

Load the approved educational CT examination. Check orientation, image quality, and the correct source series before creating a segmentation.

### 2. Open Segment Editor

Create a new segmentation associated with the CT volume. Confirm that the segmentation geometry matches the intended source image.

### 3. Create and name the segments

Create separate segments named `Right Lung`, `Left Lung`, `Body`, and `Trachea`. Select each segment deliberately before editing.

### 4. Use Threshold for an initial candidate

Explore an intensity range that highlights air-containing regions in the CT image. Review which desired and undesired areas are selected. Do not assume the threshold alone separates the lungs from external air or the airway.

### 5. Place seeds with Paint

Add representative seed regions to the right lung, left lung, body, and trachea. Place seeds away from uncertain boundaries and distribute them across relevant slices when necessary.

### 6. Run Grow from Seeds

Start **Preview** and inspect the proposed separation. Enable **Auto Update** when iterative seed refinement is helpful. Add or adjust seeds where the preview crosses an anatomical boundary or misses a region.

### 7. Apply the preview

Use **Apply** only after the right lung, left lung, body, and trachea are separated plausibly throughout the reviewed slices. Continue to treat the result as requiring quality control.

### 8. Review the 3D visualization

Display the generated segments in the 3D view. Rotate the representation and look for unexpected connections, missing regions, asymmetry caused by segmentation errors, or implausible surfaces. Return to slice views to investigate defects.

### 9. Calculate Segment Statistics

Open Segment Statistics, select the segmentation and correct CT scalar volume, and calculate results. Observe volume, voxel count, and mean HU for each relevant segment. Confirm units and segment names before interpreting or exporting any table.

## Quality Checklist

Before accepting the first lung segmentation:

- [ ] The correct CT series and segmentation geometry were selected.
- [ ] Right lung and left lung are stored as separate, correctly named segments.
- [ ] Body and trachea seeds supported the intended separation.
- [ ] Threshold selection was reviewed rather than accepted automatically.
- [ ] Grow from Seeds preview was checked before Apply.
- [ ] Auto Update behavior was understood during seed refinement.
- [ ] Boundaries were inspected in axial, coronal, and sagittal planes.
- [ ] The 3D view was used to find global defects, followed by slice-level review.
- [ ] Segment Statistics used the intended segmentation and CT scalar volume.
- [ ] Volume units, voxel counts, and mean HU values were identified correctly.
- [ ] No measurement was treated as proof of segmentation accuracy.

Common errors to avoid:

- painting seeds in the wrong active segment;
- using too few seeds to represent a region;
- placing seeds across uncertain or incorrect boundaries;
- applying Grow from Seeds before reviewing the complete preview;
- confusing Preview or Auto Update with final acceptance;
- allowing right and left lungs to remain unintentionally connected;
- relying only on the 3D surface for quality assessment;
- calculating statistics against the wrong scalar volume;
- reporting volume or mean HU without reviewing the mask and units.

## Lessons Learned

- Segment Editor manages multiple labeled structures within one segmentation.
- Threshold can accelerate initialization but does not provide anatomical understanding.
- Paint can define seeds and make targeted additions, but requires control of the active segment.
- Grow from Seeds is an iterative process of seed placement, preview, review, and refinement.
- Preview, Auto Update, and Apply serve different purposes and should not be treated as interchangeable.
- Separating the lungs, body, and trachea requires both image information and intentional labels.
- The 3D view helps identify global problems, while slice views remain essential for boundary review.
- Segment Statistics converts the mask into quantitative outputs whose reliability depends on segmentation quality.

## Future Course Notes

- Use a synthetic or appropriately licensed chest CT for the guided demonstration.
- Show an intentionally poor seed distribution and how the preview changes after refinement.
- Emphasize active-segment selection before every Paint operation.
- Include a short comparison between voxel count and physical volume.
- Demonstrate how choosing the wrong scalar volume affects the meaning of mean intensity.
- Add a worksheet for recording segment names, source volume, volume, voxel count, and mean HU.
- Reserve detailed quality-control and manual-editing criteria for Lesson 04.
- Continue next with a more standardized segmentation pipeline using Islands, Logical Operators, Margin, and Smoothing.

