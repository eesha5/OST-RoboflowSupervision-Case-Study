# Based on the minimal example in roboflow/supervision#2578
import numpy as np
import supervision as sv

def box(tid, y):
    return sv.Detections(
        xyxy=np.array([[80.0, y, 120.0, y + 40]]),
        confidence=np.array([0.9]),
        class_id=np.array([0]),
        tracker_id=np.array([tid]),
    )

# two different unconfirmed objects, both id -1, on opposite sides of the line
lz = sv.LineZone(start=sv.Point(0, 100), end=sv.Point(200, 100))
for tid, y in [(-1, 20), (-1, 160), (-1, 20), (-1, 160), (-1, 20), (-1, 160)]:
    lz.trigger(box(tid, y))
print(lz.in_count, lz.out_count)   # 2 3

# identical motion with real ids is correctly quiet
lz2 = sv.LineZone(start=sv.Point(0, 100), end=sv.Point(200, 100))
for tid, y in [(1, 20), (2, 160), (1, 20), (2, 160), (1, 20), (2, 160)]:
    lz2.trigger(box(tid, y))
print(lz2.in_count, lz2.out_count)  # 0 0