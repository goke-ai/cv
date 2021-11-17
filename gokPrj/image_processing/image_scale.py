import cv2 as cv
from utilities import show_in_matplotlib


def double_size(img):
    '''
    double the size on an image
    '''
    (height, width) = img.shape[:2]
    img_resized = cv.resize(img, (width * 2, height * 2),
                            interpolation=cv.INTER_AREA)
    return img_resized


def half_size(img):
    return cv.resize(img, None, fx=.5, fy=.5,
                     interpolation=cv.INTER_NEAREST)


def enlarge(img, fx, fy):
    '''
    enlarge an image by factor fx and fy on width and height respectively

    @fx: width factor
    @fy: height factor

    '''
    img_resized = cv.resize(img,  None, fx=fx, fy=fx,
                            interpolation=cv.INTER_AREA)
    return img_resized

def reduce(img, fx, fy):
    '''
    reduce an image by factor fx and fy on width and height respectively
    
    '''
    img_resized = cv.resize(img,  None, fx=fx, fy=fx,
                            interpolation=cv.INTER_NEAREST)
    return img_resized

if __name__ == "__main__":
    img = cv.imread('color_img.png')
    show_in_matplotlib(img)

    img_resized = double_size(img)
    show_in_matplotlib(img_resized)

    img_resized = enlarge(img, 2,  2)
    show_in_matplotlib(img_resized)

    img_resized = half_size(img)
    show_in_matplotlib(img_resized, title="INTER_AREA")

    img_resized = reduce(img, .5, .5)
    show_in_matplotlib(img_resized)