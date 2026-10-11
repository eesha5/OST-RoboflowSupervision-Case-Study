# Based on the minimal example in roboflow/supervision#2674
import numpy as np
import supervision as sv
from supervision._cv2 import BACKEND_NAME

detections = sv.Detections(
    xyxy=np.array([[20.0, 20.0, 80.0, 60.0]]),
    class_id=np.array([0]),
    confidence=np.array([0.9]),
)
scene = np.zeros((80, 100, 3), dtype=np.uint8)
painted = sv.BoxAnnotator().annotate(scene, detections).any(axis=2)
ys, xs = np.where(painted)

print(f"backend        : {BACKEND_NAME}")
print(f"painted pixels : {int(painted.sum())}")
print(f"painted bbox   : x {xs.min()}-{xs.max()}, y {ys.min()}-{ys.max()}")