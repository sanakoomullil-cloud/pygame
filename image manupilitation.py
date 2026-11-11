import os
import cv2

# Automatically finds sample.jpg in the exact same folder as your script
folder = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(folder, "background.jpg")

img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found at", img_path)
else:
    h, w = img.shape[:2]
    print("Success! Image size:", w, "x", h)

