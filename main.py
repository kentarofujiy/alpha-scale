from __future__ import division

import os

import cv2
import numpy as np

target_img = cv2.imread('./model.png', cv2.IMREAD_UNCHANGED)
image_list = []
for root, dirs, files in os.walk("./origin"):
    for fname in files:
        image_list.append(fname)
        print(fname)
print(image_list)

for model in image_list:
    print("model : ", model)


    filename = model
    guy_img = cv2.imread('./origin/' + filename, cv2.IMREAD_UNCHANGED)

    a = np.where(guy_img > 0)
    b = np.where(target_img == 129)  # picked one of the channels in your image
    bbox_guy = np.min(a[0]), np.max(a[0]), np.min(a[1]), np.max(a[1])
    bbox_mask = np.min(b[0]), np.max(b[0]), np.min(b[1]), np.max(b[1])

    guy = guy_img[bbox_guy[0]:bbox_guy[1], bbox_guy[2]:bbox_guy[3], :]
    target = target_img[bbox_mask[0]:bbox_mask[1], bbox_mask[2]:bbox_mask[3], :]

    guy_h, guy_w, _ = guy.shape
    mask_h, mask_w, _ = target.shape
    fy = mask_h / guy_h
    fx = guy_w / mask_w
    height = (guy_h / fx)
    width = (guy_w / fx)
    print(fx)
    print(fy)
    print('width : ', width)
    print('height : ', height)
    scaled_guy = cv2.resize(guy, (round(width), round(height) ), interpolation=cv2.INTER_AREA)
    cv2.imwrite("./target/" + filename, scaled_guy)
cv2.waitKey(0)
