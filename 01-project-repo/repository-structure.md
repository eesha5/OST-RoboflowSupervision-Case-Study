# Repository Structure Investigation

**Investigated by:** Mahek Mishra — Member 1
**Investigation date:** 11 October 2026
**Official repository:** https://github.com/roboflow/supervision
**Branch inspected:** develop

## Main Folders

| Folder | Purpose |
|---|---|
| src/supervision/ | Python implementation of the library |
| tests/ | Automated tests for library behaviour |
| docs/ | Documentation pages and usage explanations |
| examples/ | Example applications demonstrating library usage |
| .github/ | GitHub workflow and collaboration configuration |

## Important Files

| File | Purpose |
|---|---|
| README.md | Introduces the project and explains basic usage |
| LICENSE.md | Contains the project's MIT license |
| pyproject.toml | Defines package metadata, dependencies, and development settings |
| mkdocs.yml | Configures the documentation website |

## Source Files Investigated

### src/supervision/detection/core.py

This file contains the Detections class.

A Detections object can store bounding-box coordinates, confidence
scores, class IDs, and other detection information. It supports
selecting a subset of detections, such as filtering by confidence.

### src/supervision/annotators/core.py

This file contains annotation classes, including BoxAnnotator.

BoxAnnotator uses detection coordinates to draw bounding boxes
on an image. My demonstration also used LabelAnnotator to add labels.

## Connection to My Demonstration

1. The program creates an image and manually supplies detection data.
2. sv.Detections stores the bounding boxes, confidence scores,
   and class IDs.
3. BoxAnnotator and LabelAnnotator draw the annotations.
4. Confidence filtering selects one of the two detections.
5. The program saves images before and after filtering.

The source investigation used the develop branch.
The local demonstration used the installed release version 0.30.9.

## Evidence

Supporting screenshots are stored in this folder's evidence directory:

- S07-repository-structure.png
- S08-source-folder.png
- S09-detections-code.png
- S10-box-annotator-code.png

## References

- https://github.com/roboflow/supervision
- https://supervision.roboflow.com/
