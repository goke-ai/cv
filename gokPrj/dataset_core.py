import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def create_dataset(datasetfilename, classNames, srcPaths):

    # list of images
    imgList = []
    labelList = []
    labelNameList = []

    for srcPath in srcPaths:        
        print(f'folder "{srcPath}"')
        for fname in os.listdir(srcPath):
            filePath = os.path.join(srcPath, fname)
            # print(filePath)
            # read
            img = cv.imread(filePath)
            imgRGB = img[:,:,::-1]

            # get last character
            fname_no_ext = os.path.splitext(fname)[0]
            label = fname_no_ext
            # print(fname_no_ext)

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
    datasetfilename = 'alldataset.npz'

    classNames = {'afiq':0, 'azureen':1, 'gavin':2, 'goke':3,  'inamul':4, 'jincheng':5, 'mahmuda':6, 'numan':7, 'saseendran':8}

    # classNames = {'A':0, 'B':1, 'C':2}

    srcPaths = [ 'all_dataset/s1', 'all_dataset/s10', 'all_dataset/s11', 'all_dataset/s12', 'all_dataset/s13', 'all_dataset/s14', 
    'all_dataset/s15', 'all_dataset/s16', 'all_dataset/s17', 'all_dataset/s18', 'all_dataset/s19', 'all_dataset/s2', 'all_dataset/s20',
    'all_dataset/s21', 'all_dataset/s22', 'all_dataset/s23', 'all_dataset/s24', 'all_dataset/s25', 'all_dataset/s26', 'all_dataset/s27',
    'all_dataset/s28', 'all_dataset/s29', 'all_dataset/s3', 'all_dataset/s30', 'all_dataset/s31', 'all_dataset/s37', 'all_dataset/s38', 
    'all_dataset/s39', 'all_dataset/s4', 'all_dataset/s40', 'all_dataset/s41', 'all_dataset/s42', 'all_dataset/s43', 'all_dataset/s45', 
    'all_dataset/s49', 'all_dataset/s5', 'all_dataset/s6', 'all_dataset/s7', 'all_dataset/s8', 'all_dataset/s9'    ]

    if create_dataset(datasetfilename, classNames, srcPaths):

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
