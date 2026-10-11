# Based on the minimal reproduction in roboflow/supervision#2658
import numpy as np
import supervision as sv
from supervision._cv2 import BACKEND_NAME

frame = np.zeros((200, 200, 3), dtype=np.uint8)
# line drawn right to left, so the label is flipped
line_zone = sv.LineZone(start=sv.Point(170, 100), end=sv.Point(30, 100))

print("backend:", BACKEND_NAME)
sv.LineZoneAnnotator(text_orient_to_line=True).annotate(
    frame=frame, line_counter=line_zone
)
print("annotate() finished without error")