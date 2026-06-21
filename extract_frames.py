import cv2
import os

video_path = "data/videos/input.mp4"
output_dir = "data/frames/degraded"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_id = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imwrite(
        f"{output_dir}/frame_{frame_id:05d}.png",
        frame
    )

    frame_id += 1

cap.release()

print(f"{frame_id} frames extracted")
