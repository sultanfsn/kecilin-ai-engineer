import os
import sys
import cv2
from ultralytics import YOLO
from ultralytics.data.loaders import LoadImagesAndVideos, LoadStreams
import random


def inference(path):
    model = YOLO('models/solution.pt')

    frame_name = path

    source = f'input/{frame_name}' # change this to desired input video

    dataset = LoadImagesAndVideos(
                    source,
                    vid_stride=1,
                )

    for path, images, info, in dataset:
        frame = images[0]

        results = model.predict(source=frame, conf=0.56)
        
        annotated_frame = results[0].plot()

        rand_name = str(random.randint(1, 9999)) + ".jpg"

        cv2.imwrite(f"output/{rand_name}", annotated_frame)
        print(os.path.realpath(f"output/{rand_name}"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [input_path]")
    else:
        input_path = sys.argv[1]
        inference(input_path)








