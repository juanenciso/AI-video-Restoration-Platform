from pathlib import Path
import time

from extract_frames import extract_frames
from restore_frames import restore_frames
from rebuild_video import rebuild_video


def main():

    start = time.time()

    video_path = Path("data/videos/short.mp4")

    frames_dir = Path("data/frames/degraded")

    restored_dir = Path("data/frames/restored")

    output_video = Path("data/restored_video.mp4")

    print("\n=== STEP 1: Extracting Frames ===")
    extract_frames(
        video_path,
        frames_dir
    )

    print("\n=== STEP 2: Restoring Frames ===")
    restore_frames(
        frames_dir,
        restored_dir
    )

    print("\n=== STEP 3: Rebuilding Video ===")
    rebuild_video(
        restored_dir / "Single_Image_Defocus_Deblurring",
        output_video
    )

    elapsed = (time.time() - start) / 60

    print("\n=== PIPELINE COMPLETE ===")
    print(f"Output video: {output_video}")
    print(f"Total time: {elapsed:.2f} min")


if __name__ == "__main__":
    main()
