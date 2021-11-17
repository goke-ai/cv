import cv2 as cv
from utilities import show_in_matplotlib


def get_channel(img, channel):
    b = img[:, :, channel]
    # g = img[:,:,1]
    # r = img[:,:,2]
    return b


def remove_channel(img, channel):
    imgCopy = img.copy()
    imgCopy[:, :, channel] = 0

    return imgCopy


def remove_channel_v0(img, channel):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    if channel == 0:
        b[:] = 0
    elif channel == 1:
        g[:] = 0
    else:
        r[:] = 0

    img_merged = cv.merge((b, g, r))

    return img_merged


if __name__ == "__main__":
    import cv2 as cv

    img = cv.imread('color_img.png')
    show_in_matplotlib(img, title='original')

    ch = 1
    b = get_channel(img, ch)
    show_in_matplotlib(b, title=f"Channel {ch} only")

    img_merged = remove_channel(img, ch)
    show_in_matplotlib(img_merged, title=f"Channel {ch} removed")
