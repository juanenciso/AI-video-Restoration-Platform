import cv2
import os

VIDEO_PATH = "data/videos/short.mp4"
OUTPUT_DIR = "data/frames/degraded"

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    output_path = os.path.join(
        OUTPUT_DIR,
        f"frame_{frame_count:05d}.png"
    )

    cv2.imwrite(output_path, frame)

    frame_count += 1

cap.release()

print(f"Extracted {frame_count} frames")
