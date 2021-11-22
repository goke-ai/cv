import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def create_canvas(height=500, width=500, bgColor=0):
    # create the image (canvas)
    canvas = np.zeros((height, width, 3), dtype='uint8')
    if bgColor != 0:
        canvas[:] = bgColor
    return canvas


def boxes_of_gray():
    # define tones
    tones = np.arange(50, 300, 50)
    # print(tones)

    # create image black of 50x50
    main_img = np.zeros((50, 50, 3), dtype='uint8')

    # build other images with different tones
    # concatenate horizontally
    for tone in tones:
        img = np.ones((50, 50, 3), dtype=np.uint8) * tone
        main_img = np.concatenate((main_img, img), axis=1)

    # plt.axis('off')
    # plt.imshow(main_img)

    # plt.show()
    cv.imwrite('gray_boxes.png', main_img)
    return main_img


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # create canvas
    img = create_canvas()

    # show canvas
    # pyplot
    # convert BGR to RGB
    imgRGB = img[:, :, ::-1]
    plt.imshow(imgRGB)

    # cleanup plt
    plt.show()

    # imgBoxes
    imgBoxes = boxes_of_gray()
    # convert BGR to RGB
    imgRGB = img[:, :, ::-1]
    plt.imshow(imgBoxes)

    plt.show()
