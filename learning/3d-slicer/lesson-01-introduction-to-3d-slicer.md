# Lesson 01 – Introduction to 3D Slicer

**Learning path:** 3D Slicer  
**Date:** Not recorded  
**Status:** Learning record  
**Scope:** Scientific learning documentation; no clinical data or patient-specific conclusions

## Objectives

- Understand the purpose of 3D Slicer as a platform for medical-image visualization and analysis.
- Recognize the main areas of the interface and change the viewing layout.
- Navigate through axial, coronal, and sagittal image planes.
- Relate the anatomical orientation labels R, L, A, P, S, and I to the displayed image.
- Understand the basic meaning of a voxel and a segmentation.
- Load an imaging examination and inspect it without modifying the source data.
- Use the 3D view as a complementary visualization area rather than a replacement for slice review.

## Scientific Background

### Purpose of 3D Slicer

3D Slicer is an open-source platform for viewing, processing, and analyzing medical images. It brings together two-dimensional slice views, three-dimensional visualization, segmentation tools, measurements, and extensible modules in one environment. In this first lesson, the focus was orientation and safe navigation rather than image processing.

The software supports research and scientific learning workflows, but opening an examination in 3D Slicer does not by itself establish a validated clinical workflow. The intended use, data governance, method, and quality controls remain important.

### Interface and layout

The interface includes a module selector, toolbars, a data or subject hierarchy, module-specific controls, slice viewers, and a 3D view. The selected layout determines which views are visible and how much screen space each receives.

Changing the layout does not change the underlying examination. It changes how the same data are presented. A layout with axial, coronal, sagittal, and 3D views is useful for learning the relationship between planes.

### Anatomical planes

- **Axial:** divides the body into superior and inferior portions.
- **Coronal:** divides the body into anterior and posterior portions.
- **Sagittal:** divides the body into right and left portions.

The three planes are linked views of the same volume. Moving through one plane changes the anatomical position being inspected, while cross-reference indicators help relate the current location across views.

### Anatomical orientation

The orientation labels describe patient directions:

- **R:** right
- **L:** left
- **A:** anterior
- **P:** posterior
- **S:** superior
- **I:** inferior

These labels should be checked instead of assuming that screen-left or screen-right always corresponds to a fixed patient side. Display conventions, view orientation, and image metadata affect presentation.

### Voxel concept

A voxel is a volume element in a three-dimensional image. It can be understood as the 3D counterpart of a pixel. Each voxel has a position, physical dimensions defined by image spacing, and an image value. Voxel dimensions may differ between the in-plane directions and slice direction.

Voxel spacing is important because counting voxels is not the same as measuring physical volume. Physical measurements depend on voxel dimensions and image geometry.

### Segmentation concept

Segmentation is the process of identifying and labeling a region of interest in an image. A segment may represent an organ, structure, lesion, or another defined region. The result is a mask connected to the geometry of the source image.

Segmentation is an interpretation based on an objective and a set of boundary rules. It is not created simply by displaying an image in 3D, and it requires review before it can support measurements or research.

## Practical Workflow

### 1. Start 3D Slicer and identify the interface

Locate the module selector, toolbar, data hierarchy, module panel, slice views, and 3D view. Observe which controls change when a different module is selected.

### 2. Load the examination

Use the appropriate loading option for the approved learning examination. Confirm that the expected image volume appears in the data hierarchy and slice viewers. Do not overwrite or alter source data during initial inspection.

### 3. Select a multi-view layout

Choose a layout that displays the axial, coronal, sagittal, and 3D views together. Confirm that each slice view has its own orientation label and slice controller.

### 4. Navigate through slices

Move through each plane using the mouse wheel or slice control. Practice zooming and panning while keeping track of the anatomical location. Return to a complete view if navigation causes loss of context.

### 5. Relate the three planes

Select an anatomical position and observe its relationship across axial, coronal, and sagittal views. Use cross-reference information when available to understand that all views represent the same volume.

### 6. Confirm anatomical orientation

Read the R, L, A, P, S, and I labels in every view. Identify patient right and left from the labels rather than from screen position alone.

### 7. Inspect the 3D view

Use the 3D window to understand where future three-dimensional representations will appear. At this stage, recognize that a loaded image volume and a segmented 3D model are different objects.

## Quality Checklist

Before finishing the introductory inspection:

- [ ] The expected examination was loaded.
- [ ] The source volume is visible in the data hierarchy.
- [ ] Axial, coronal, and sagittal views were identified correctly.
- [ ] R, L, A, P, S, and I labels were checked.
- [ ] Navigation, zoom, and pan were practiced without changing source data.
- [ ] The relationship between slice views and the 3D view was understood.
- [ ] A voxel was distinguished from a pixel and from physical volume.
- [ ] Segmentation was understood as a labeled mask, not merely a 3D display.

Common errors to avoid:

- assuming patient right and left from screen position without checking labels;
- confusing the coronal and sagittal planes;
- interpreting voxel count as physical volume without considering spacing;
- expecting a 3D model to exist before a structure has been segmented;
- loading the wrong series and continuing without checking the data hierarchy;
- using only one plane to understand a three-dimensional structure.

## Lessons Learned

- 3D Slicer organizes imaging, visualization, segmentation, and analysis in a modular interface.
- Axial, coronal, and sagittal views provide complementary information about the same volume.
- Anatomical orientation labels are essential for safe navigation.
- A voxel has physical dimensions and an image value; it is more than a point on the screen.
- Segmentation creates a labeled representation of a defined region and requires an explicit objective.
- The 3D view supports spatial understanding, but slice views remain necessary for detailed inspection.
- Confirming the examination and orientation is a prerequisite for later segmentation work.

## Future Learning Directions

- Include an annotated interface image using only public or synthetic content.
- Add a short self-assessment for identifying each anatomical plane and orientation label.
- Document the difference between pixels, voxels, voxel count, and physical volume with a simple diagram.
- Add a navigation record that uses the same anatomical point across all three planes.
- Reinforce that loading data, creating a segmentation, and generating a 3D representation are separate stages.
- Record the exact 3D Slicer version and the approved example dataset when preparing the scientific learning documentation.
- Continue next with the first documented lung-segmentation exercise using Segment Editor.
