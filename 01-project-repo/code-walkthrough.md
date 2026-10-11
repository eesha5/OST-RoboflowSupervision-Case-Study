# Code Walkthrough: Detections and BoxAnnotator

## Source Files Inspected
- src/supervision/detection/core.py
- src/supervision/annotators/core.py

Branch inspected: develop
Investigation date: 11 October 2026

## 1. Detections
The Detections class stores information about detected objects.

Important fields include:
- xyxy: bounding-box coordinates, ordered as left, top, right, bottom.
- confidence: a confidence score associated with each detection.
- class_id: a numeric identifier for the object's class.

## 2. BoxAnnotator
BoxAnnotator draws bounding boxes on an image using the supplied detections.

Its annotate method receives:
- scene: the image to annotate.
- detections: the detection information.

It returns the annotated image.

## 3. Basic Flow
1. Supply an image and detection information.
2. Store the detection information in a Detections object.
3. Pass the image and Detections object to BoxAnnotator.
4. Obtain an image with bounding boxes drawn on it.

BoxAnnotator draws supplied detections; it does not predict objects itself.

## Evidence
- S09-detections-code.png
- S10-box-annotator-code.png

## Practical Status
Source code inspected. The local demonstration has not been run yet.

## References
https://github.com/roboflow/supervision/blob/develop/src/supervision/detection/core.py
https://github.com/roboflow/supervision/blob/develop/src/supervision/annotators/core.py
