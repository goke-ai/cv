import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def create_dataset(datasetfilename, classNames):

    # list of images
    imgList = []
    labelList = []
    labelNameList = []

    # read image files from folder
    srcPath = "rawdata"
    for fname in os.listdir(srcPath):
        filePath = os.path.join(srcPath, fname)
        # read
        img = cv.imread(filePath)
        imgRGB = img[:,:,::-1]

        # get last character
        fname_no_ext = os.path.splitext(fname)[0]
        label = fname_no_ext[-1]

        # append image
        imgList.append(imgRGB)
        labelList.append(classNames[label])
        labelNameList.append(label)

    images = np.array(imgList, dtype='object')
    labels = np.array(labelList)
    labelnames = np.array(labelNameList)
    np.savez_compressed(datasetfilename, images=images, labels=labels, labelnames=labelnames)

    return True


if __name__ == "__main__":
    # save dataset
    datasetfilename = 'gokedataset.npz'

    # classNames = {'afiq':0, 'azureen':1, 'gavin':2, 'goke':3,  'inamul':4, 'jincheng':5, 'mahmuda':6, 'numan':7, 'saseendran':8}

    classNames = {'A':0, 'B':1, 'C':2}


    if create_dataset(datasetfilename, classNames):

        data = np.load(datasetfilename, allow_pickle=True)

        imgList = data['images']
        labelList = data['labels']
        labelNameList = data['labelnames']

        # display first and 2nd image
        img = imgList[0]
        label = labelList[0]
        labelName = labelNameList[0]
        # convert BGR to RGB
        # imgRGB = img[:, :, ::-1]
        # show
        # plt.imshow(imgRGB)
        plt.imshow(img)
        plt.title(str(label) + ':' + labelName)
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
