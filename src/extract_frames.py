import cv2
from pathlib import Path

def extract_frames(video_path, output_dir):

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_path = output_dir / f"frame_{frame_count:05d}.png"

        cv2.imwrite(str(frame_path), frame)

        frame_count += 1

    cap.release()

    print(f"Extracted {frame_count} frames")

    return frame_count
