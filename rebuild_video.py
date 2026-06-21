import cv2
import glob

frames = sorted(
    glob.glob("data/frames/restored/*.png")
)

frame = cv2.imread(frames[0])

height, width, _ = frame.shape

video = cv2.VideoWriter(
    "data/restored/output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    30,
    (width, height)
)

for f in frames:
    img = cv2.imread(f)
    video.write(img)

video.release()
