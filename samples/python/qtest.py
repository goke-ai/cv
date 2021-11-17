import cv2 as cv
import matplotlib.pyplot as plt
import os


img = cv.imread('samples/data/lena.jpg')

print(img)
print(os.getcwd())

# plt.imshow(img)
# plt.show()