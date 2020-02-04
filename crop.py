import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[3:12, 24:33]
print(cropped.shape)
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)