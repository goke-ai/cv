import numpy as np

def create_canvas(height=500, width=500, bgColor=0):
    # create the image (canvas)
    canvas = np.zeros((height, width, 3), dtype='uint8')
    if bgColor != 0:
        canvas[:] = bgColor
    return canvas


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # create canvas
    img = create_canvas()

    # show canvas
    # pyplot
    # convert BGR to RGB
    imgRGB = img[:,:,::-1]
    plt.imshow(imgRGB)

    # cleanup plt
    plt.show()