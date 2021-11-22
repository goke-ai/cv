import cv2 as cv
import matplotlib.pyplot as plt


def binary(imgGray, thresh=50):
    ret, thresh_img = cv.threshold(imgGray, thresh, 255, cv.THRESH_BINARY)
    return ret, thresh_img


def binary_inv(imgGray, thresh=50):
    ret, thresh_img = cv.threshold(imgGray, thresh, 255, cv.THRESH_BINARY_INV)
    return ret, thresh_img


def trunc(imgGray, thresh=50):
    ret, thresh_img = cv.threshold(imgGray, thresh, 255, cv.THRESH_TRUNC)
    return ret, thresh_img


def tozero(imgGray, thresh=50):
    ret, thresh_img = cv.threshold(imgGray, thresh, 255, cv.THRESH_TOZERO)
    return ret, thresh_img


def tozero_inv(imgGray, thresh=50):
    ret, thresh_img = cv.threshold(imgGray, thresh, 255, cv.THRESH_TOZERO_INV)
    return ret, thresh_img


if __name__ == "__main__":

    import sys

    filePath = 'gray_boxes.png'

    if len(sys.argv) > 1:
        filePath = sys.argv[1]

    # load or read the image
    img = cv.imread(filePath)

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, imgThreshed = binary(imgGray)

    plt.subplot(3, 3, 1)
    imgRGB = img[:, :, ::-1]
    plt.imshow(imgRGB)
    plt.title('original')

    plt.subplot(3, 3, 2)
    imgRGB = cv.cvtColor(imgGray, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title('gray')

    plt.subplot(3, 3, 3)
    imgRGB = cv.cvtColor(imgThreshed, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title(f'thresh={ret}, maxval=255')

    #
    ret, imgThreshed = binary(imgGray, 256//2)
    #
    plt.subplot(3, 3, 4)
    imgRGB = cv.cvtColor(imgThreshed, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title(f'thresh={ret}, maxval=255')

    #
    ret, imgThreshed = binary_inv(imgGray, 256//2)
    #
    plt.subplot(3, 3, 5)
    imgRGB = cv.cvtColor(imgThreshed, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title(f'thresh={ret}, maxval=255')

    #
    ret, imgThreshed = trunc(imgGray, 256//2)
    #
    plt.subplot(3, 3, 6)
    imgRGB = cv.cvtColor(imgThreshed, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title(f'thresh={ret}, maxval=255')

    #
    ret, imgThreshed = tozero(imgGray, 256//2)
    #
    plt.subplot(3, 3, 7)
    imgRGB = cv.cvtColor(imgThreshed, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title(f'thresh={ret}, maxval=255')
    #
    ret, imgThreshed = tozero_inv(imgGray, 256//2)
    #
    plt.subplot(3, 3, 8)
    imgRGB = cv.cvtColor(imgThreshed, cv.COLOR_GRAY2RGB)
    plt.imshow(imgRGB)
    plt.title(f'thresh={ret}, maxval=255')

    #
    plt.tight_layout()
    plt.show()
