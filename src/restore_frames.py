import subprocess
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RESTORMER_DIR = PROJECT_ROOT / "third_party" / "Restormer"

INPUT_DIR = PROJECT_ROOT / "data" / "test_frames"

OUTPUT_DIR = PROJECT_ROOT / "data" / "test_restored_batch"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

frames = sorted(INPUT_DIR.glob("*.png"))

print(f"Found {len(frames)} frames")

times = []

for frame in frames:
    print(f"\nProcessing {frame.name}")

    start = time.time()

    cmd = [
        "python",
        "demo.py",
        "--task",
        "Single_Image_Defocus_Deblurring",
        "--input_dir",
        str(frame),
        "--result_dir",
        str(OUTPUT_DIR)
    ]

    subprocess.run(
        cmd,
        cwd=RESTORMER_DIR
    )

    elapsed = time.time() - start

    times.append(elapsed)

    print(f"Finished in {elapsed:.2f} sec")

print("\nSummary")
print(f"Frames: {len(times)}")
print(f"Average: {sum(times)/len(times):.2f} sec")
print(f"Total: {sum(times)/60:.2f} min")
