import cv2 as cv
import matplotlib.pyplot as plt

def show_in_matplotlib(imgBGR, figsize=(6,8), title=None):
    
    imgRGB = cv.cvtColor(imgBGR, cv.COLOR_BGR2RGB)
    # imgRGB = toRGB(img)
    plt.figure(figsize=figsize)
    
    plt.imshow(imgRGB)
    plt.title(title)
    plt.show()
