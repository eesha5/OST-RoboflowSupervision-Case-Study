# Main Features of Supervision

## 1. Detections
Stores information about detected objects, including bounding-box coordinates, confidence scores, and class IDs.

## 2. Annotators
Draws bounding boxes, labels, and other visual information on images or video frames.

## 3. Zones
Helps check whether detections are inside a selected region or cross a defined line.

## 4. Dataset Tools
Provides tools to load, split, merge, and save datasets in supported formats.

## Completed Local Demonstration

I ran a Python demonstration using Supervision 0.30.9 on Windows
with Python 3.12.7.

The demonstration used two manually supplied detections with
confidence scores of 0.95 and 0.60. BoxAnnotator and LabelAnnotator
drew bounding boxes and labels for both detections.

Applying a confidence threshold of 0.80 retained one detection.
The generated images confirmed the change from two annotated
detections to one.

The code, dependencies, terminal output, generated images, and
run instructions are available in the repository's demo folder.

This demonstration tested annotation and confidence filtering.
It did not use a trained object-detection model.

## References
https://github.com/roboflow/supervision
https://supervision.roboflow.com/
