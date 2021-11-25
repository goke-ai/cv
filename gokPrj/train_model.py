
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

datasetFileName = "gokedataset.npz"

with np.load(datasetFileName, allow_pickle=True) as data:
    dataImages = data['images']
    dataLabelAsName = data['labels']
    dataLabels = dataLabelAsName

classNames = ['A','B','C']


# Split the data up in train and test sets
trainImages, testImages, trainLabels, testLabels = train_test_split(dataImages, dataLabels, test_size=0.30, random_state=42)


print(tf.__version__)
print(dataImages.shape)
print(dataLabels)

print(trainImages.shape)
print(testImages.shape)
