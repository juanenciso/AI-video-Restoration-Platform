import cv2
from pathlib import Path

def rebuild_video(
    input_dir,
    output_video,
    fps=30
):

    frames = sorted(Path(input_dir).glob("*.png"))

    if not frames:
        raise ValueError("No frames found")

    first = cv2.imread(str(frames[0]))

    height, width = first.shape[:2]

    video = cv2.VideoWriter(
        str(output_video),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    for frame_path in frames:

        frame = cv2.imread(str(frame_path))

        video.write(frame)

    video.release()

    print(f"Video saved at {output_video}")
