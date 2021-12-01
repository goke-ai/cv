# %%


# %% [markdown]
# # Chapter 31

# %% [markdown]
# # Keras and OpenCV II

# %% [markdown]
# 1. Keras Model Saving 
# 2. Keras Model Loading

# %% [markdown]
# ## Keras Model Saving

# %% [markdown]
# ## Keras Model Loading

# %%
import cv2 as cv
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# %%

def fixImage(imgRGB):
    # model expect shape of image to be 200x200
    desiredShape = (200, 200, 3)

    N = 1

    shape = (N, desiredShape[0], desiredShape[1], desiredShape[2])

    y = np.empty(shape, dtype='uint8')

    y[0] = cv.resize(imgRGB, [200,200], interpolation=cv.INTER_NEAREST)

    return y



# %%

def fixImages(imgRGBs):
    # model expect shape of image to be 200x200
    desiredShape = (200, 200, 3)

    N = len(imgRGBs)

    shape = (N, desiredShape[0], desiredShape[1], desiredShape[2])

    y = np.empty(shape, dtype='uint8')

    for i in range(N):
        y[i] = cv.resize(imgRGBs[i], [200,200], interpolation=cv.INTER_NEAREST)

    return y



# %%

# 
classes = ['afiq',
 'azureen',
 'gavin',
 'goke',
 'inamul',
 'jincheng',
 'mahmuda',
 'numan',
 'saseendran']


# %%

# load model
exportPath = '../advance/tf_model/4_max'
model = tf.keras.models.load_model(exportPath)

# Check its architecture
model.summary()


# %%

# prepare image according to model shape
img = cv.imread('dataset/x (6).png')
print(img.shape)
imgRGB = img[:,:,::-1]


# %%

imgRGB = fixImage(imgRGB)

imgRGB.shape

# %%


# predict
probabilityModel = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probabilityModel.predict(imgRGB)

print('predictions: ', predictions[0])

# %%

# highest index
imax = np.argmax(predictions[0])


# %%

# find index in class
# corresponding label
label = classes[imax]


# %%

plt.imshow(imgRGB.squeeze())
plt.title(label)
plt.axis('off')
plt.show()

# %% [markdown]
# 


