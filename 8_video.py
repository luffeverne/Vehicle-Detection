# -*- coding: utf-8 -*-
import imageio
from car.train import load_model
from car.detect import ImgDetector, VideoDetector
from car.data import list_files
from car.utils import plot_images

import cv2
import numpy as np


def files_to_images(files):
    import numpy as np
    images = []
    for filename in files:
        image = cv2.imread(filename)
        images.append(image)
    images = np.array(images)
    return images

START = 890
START = 877

if __name__ == "__main__":
    img_files = list_files("project_video", pattern="*.jpg", random_order=False, recursive_option=False)
    imgs = files_to_images(img_files)[START:START+1]
    
    d = ImgDetector(classifier=load_model("model_v4.pkl"))
    
    count = START
    for img in imgs:
        img_draw = d.run(img)
        
        plot_images([img, img_draw, d._heat_map._heat_map])
        x1, y1, x2, y2 = d.heat_boxes[0]
        w = x2-x1
        h = y2-y1
        print(w, h, w/h)

