
import cv2 as cv
import matplotlib.pyplot as plt
from color_component import get_channel, remove_channel
from gokPrj.image_processing.image_scale import enlarge

img = cv.imread('color_img.png')

imgRGB = img[:, :, ::-1]
plt.subplot(3, 1, 1)
plt.imshow(imgRGB)
plt.title("original")

ch = 1
imgSingleChannel = get_channel(img, ch)
imgRGB = cv.cvtColor(imgSingleChannel, cv.COLOR_BGR2RGB)
plt.subplot(3, 1, 2)
plt.imshow(imgRGB)
plt.title(f"Channel {ch} only")


imgChannelRemoved = remove_channel(img, ch)
imgRGB = imgChannelRemoved[:, :, ::-1]
plt.subplot(3, 1, 3)
plt.imshow(imgRGB)
plt.title(f"Channel {ch} removed")


plt.tight_layout()
plt.show()

img3ple = enlarge(img, 3,3)
imgRGB = img3ple[:, :, ::-1]
plt.imshow(imgRGB)
plt.title(f"Triple")


plt.tight_layout()
plt.show()

