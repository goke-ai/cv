import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def create_dataset(datasetfilename):

    # list of images
    imgList = []
    labelList = []

    # read image files from folder
    srcPath = "rawdata"
    for fname in os.listdir(srcPath):
        filePath = os.path.join(srcPath, fname)
        # read
        img = cv.imread(filePath)

        # get last character
        fname_no_ext = os.path.splitext(fname)[0]
        label = fname_no_ext[-1]

        # append image
        imgList.append(img)
        labelList.append(label)

    images = np.array(imgList, dtype='object')
    labels = np.array(labelList, dtype='object')
    np.savez_compressed(datasetfilename, images=images, labels=labels)

    return True


if __name__ == "__main__":
    # save dataset
    datasetfilename = 'gokedataset.npz'

    if create_dataset(datasetfilename):

        data = np.load(datasetfilename, allow_pickle=True)

        imgList = data['images']
        labelList = data['labels']

        # display first and 2nd image
        img = imgList[0]
        label = labelList[0]
        # convert BGR to RGB
        imgRGB = img[:, :, ::-1]
        # show
        plt.imshow(imgRGB)
        plt.title(label)
        # show
        plt.show()

        # #
        # img = imgList[1]
        # label = labelList[1]
        # # convert BGR to RGB
        # imgRGB = img[:, :, ::-1]
        # # show
        # plt.imshow(imgRGB)
        # plt.title(label)
        # # show
        # plt.show()
