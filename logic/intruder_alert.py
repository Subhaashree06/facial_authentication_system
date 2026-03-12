import cv2
import os
from datetime import datetime
import winsound


def intruder_alert(frame):
    os.makedirs("intruder", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"intruder/intruder_{timestamp}.jpg"

    cv2.imwrite(path, frame)

    for _ in range(3):
        winsound.Beep(1000, 300)

    print("INTRUDER ALERT! Image saved.")
