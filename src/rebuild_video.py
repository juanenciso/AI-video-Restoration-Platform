import cv2
from pathlib import Path

INPUT_DIR = Path(
    "data/test_restored_batch/Single_Image_Defocus_Deblurring"
)

OUTPUT_VIDEO = "data/restored_video.mp4"

frames = sorted(INPUT_DIR.glob("*.png"))

if not frames:
    raise ValueError("No frames found")

first = cv2.imread(str(frames[0]))

height, width = first.shape[:2]

video = cv2.VideoWriter(
    OUTPUT_VIDEO,
    cv2.VideoWriter_fourcc(*"mp4v"),
    30,
    (width, height)
)

for frame_path in frames:
    frame = cv2.imread(str(frame_path))
    video.write(frame)

video.release()

print(f"Video saved at: {OUTPUT_VIDEO}")
