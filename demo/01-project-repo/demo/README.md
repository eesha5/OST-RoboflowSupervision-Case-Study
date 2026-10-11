# Member 1: Supervision Demonstration

**Author:** Mahek Mishra
**Environment used:** Windows, Python 3.12.7, Supervision 0.30.9

## Purpose

This demonstration shows how Supervision stores detections,
draws bounding boxes and labels, and filters detections by confidence.

The image and detection values are created manually.
No trained object-detection model is used.

## How to Run

Download the group repository and open a terminal inside its demo folder.

Create a virtual environment:

    python -m venv .venv

Activate it in Windows Command Prompt:

    .venv\Scripts\activate

Install the recorded dependencies:

    python -m pip install -r requirements.txt

Run the demonstration:

    python member1_demo.py

The generated images are saved inside the output folder.

## Code Flow

1. NumPy creates a blank image.
2. Two grey rectangles are drawn on the image.
3. sv.Detections stores two manually supplied bounding boxes,
   confidence scores, and class IDs.
4. BoxAnnotator draws bounding boxes.
5. LabelAnnotator adds labels.
6. A confidence threshold of 0.80 selects the higher-confidence detection.
7. The original and annotated images are saved.

## Observed Results

| Output file | Observed result |
|---|---|
| output/input.png | Two grey rectangles without detection annotations |
| output/annotated.png | Both detections have bounding boxes and labels |
| output/filtered.png | Only the detection with confidence 0.95 is annotated |

There were two detections before filtering and one after filtering.
The detection with confidence 0.60 was excluded by the 0.80 threshold.

Filtering removes the excluded detection's annotation.
It does not erase the grey rectangle from the image.

## Files

- member1_demo.py: demonstration code
- requirements.txt: recorded Python dependencies
- run-output.txt: saved terminal output from the local run
- output/: generated images

## Scope

The local run demonstrates annotation and confidence filtering.
It does not test model prediction accuracy, tracking, dataset conversion,
or the complete upstream test suite.
