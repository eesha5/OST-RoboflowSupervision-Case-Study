from pathlib import Path
import platform
import sys

import cv2
import numpy as np
import supervision as sv

output = Path(__file__).resolve().parent / "output"
output.mkdir(exist_ok=True)

# Create an image with two artificial objects.
image = np.full((400, 600, 3), 255, dtype=np.uint8)
cv2.rectangle(image, (70, 100), (230, 300), (180, 180, 180), -1)
cv2.rectangle(image, (330, 130), (510, 290), (120, 120, 120), -1)

# Manually supplied example detections, not model predictions.
detections = sv.Detections(
    xyxy=np.array([
        [70, 100, 230, 300],
        [330, 130, 510, 290]
    ], dtype=np.float32),
    confidence=np.array([0.95, 0.60], dtype=np.float32),
    class_id=np.array([0, 1], dtype=int)
)

def annotate(items):
    result = sv.BoxAnnotator().annotate(
        scene=image.copy(),
        detections=items
    )
    labels = [
        f"Object {int(class_id)}: {score:.2f}"
        for class_id, score in zip(items.class_id, items.confidence)
    ]
    return sv.LabelAnnotator().annotate(
        scene=result,
        detections=items,
        labels=labels
    )

filtered = detections[detections.confidence >= 0.80]

results = {
    "input.png": image,
    "annotated.png": annotate(detections),
    "filtered.png": annotate(filtered)
}

for filename, result in results.items():
    if not cv2.imwrite(str(output / filename), result):
        raise RuntimeError(f"Could not save {filename}")

print("Operating system:", platform.platform())
print("Python:", sys.version.split()[0])
print("Supervision:", sv.__version__)
print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Original detections:", len(detections))
print("Detections after filtering:", len(filtered))
print("Images saved in:", output)