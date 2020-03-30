# # import cv2
# # import numpy as np
# # import os
# # from random import shuffle
# # from tqdm import tqdm

# # TRAIN_DIR = 'chest_xray\chest_xray\train'
# # TEST_DIR = 'chest_xray\chest_xray\test'
# # IMG_SIZE = 50

# # def label_img(img):
# #     word_label = img.split('.') 



from keras.preprocessing.image import ImageDataGenerator 
from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D 
from keras.layers import Activation, Dropout, Flatten, Dense 
from keras import backend as K 
import keras

# # #datagen = ImageDataGenerator(
# # #        rotation_range=40, #rotation_range is a value in degrees (0-180), a range within which to randomly rotate pictures
# # #        width_shift_range=0.2, #width_shift and height_shift are ranges (as a fraction of total width or height) within which to randomly translate pictures vertically or horizontally
# # #        height_shift_range=0.2,
# # #        rescale=1./255,#rescale is a value by which we will multiply the data before any other processing. Our original images consist in RGB coefficients in the 0-255, but such values would be too high for our models to process (given a typical learning rate), so we target values between 0 and 1 instead by scaling with a 1/255. factor.
# # #        shear_range=0.2,#shear_range is for randomly applying shearing transformations
# # #        zoom_range=0.2,#zoom_range is for randomly zooming inside pictures
# # #        horizontal_flip=True,#horizontal_flip is for randomly flipping half of the images horizontally --relevant when there are no assumptions of horizontal assymetry (e.g. real-world pictures).
# # #        fill_mode='nearest')#fill_mode is the strategy used for filling in newly created pixels, which can appear after a rotation or a width/height shift.


from keras import layers
from keras import models
from keras import optimizers
import tensorflow as tf
# print(tf.test.is_gpu_available())
# # # #model = models.Sequential()
# # # #model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
# # # #model.add(layers.MaxPooling2D((2, 2)))
# # # #model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# # # #model.add(layers.MaxPooling2D((2, 2)))
# # # #model.add(layers.Conv2D(64, (3, 3), activation='relu'))

img_width, img_height = 224, 224

train_data_dir = 'chest_xray/chest_xray/train'
validation_data_dir = 'chest_xray/chest_xray/test'
nb_train_samples = 5216 
nb_validation_samples = 624
epochs = 2
batch_size = 1


if K.image_data_format() == 'channels_first': 
    input_shape = (3, img_width, img_height) 
else: 
    input_shape = (img_width, img_height, 3) 
# print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

from keras.applications.mobilenet_v2 import MobileNetV2
model = MobileNetV2(weights=None, classes=2)
# model = Sequential() 
# model.add(Conv2D(64, (3, 3), input_shape=input_shape)) 
# model.add(Activation('relu')) 
# model.add(Conv2D(64, (3, 3))) 
# model.add(Activation('relu')) 
# model.add(MaxPooling2D(pool_size=(2, 2))) 

# model.add(Conv2D(128, (3, 3))) 
# model.add(Activation('relu'))
# model.add(Conv2D(128, (3, 3))) 
# model.add(Activation('relu')) 
# model.add(MaxPooling2D(pool_size=(2, 2)))

# model.add(Conv2D(256, (3, 3))) 
# model.add(Activation('relu')) 
# model.add(Conv2D(256, (3, 3))) 
# model.add(Activation('relu')) 
# model.add(MaxPooling2D(pool_size=(2, 2))) 

# model.add(Flatten()) 
# model.add(Dense(4096)) 
# model.add(Activation('relu')) 
# model.add(Dense(500)) 
# model.add(Activation('relu'))  
# model.add(Dropout(0.5))
# model.add(Dense(2)) 
# model.add(Activation('sigmoid')) 

# adagrad = optimizers.Adagrad(learning_rate=0.01)

# model.compile(loss='mean_squared_error', 
#               optimizer=adagrad, 
#               metrics=['accuracy']) 
# model.summary()
# model = models.load_model('fuck.h5')
# model.summary()
# train_datagen = ImageDataGenerator(zoom_range=0.2,rescale=1. / 255) 
  
# test_datagen = ImageDataGenerator(rescale=1. / 255) 
  
# train_generator = train_datagen.flow_from_directory( 
#     train_data_dir, 
#     shuffle=True,
#     target_size=(img_width, img_height), 
#     batch_size=batch_size, 
#     class_mode='categorical') 
# # print(train_generator)
# validation_generator = test_datagen.flow_from_directory( 
#     validation_data_dir, 
#     target_size=(img_width, img_height), 
#     batch_size=batch_size, 
#     class_mode='categorical') 
  
# model.fit_generator( 
#     train_generator, 
#     steps_per_epoch=nb_train_samples // batch_size, 
#     epochs=epochs, 
#     validation_data=validation_generator, 
#     validation_steps=nb_validation_samples // batch_size) 
import json
# model.save('model_saved.h5') 
import tensorflowjs as tfjs
# with open()
# with open('model.json', 'r') as json_file:
#     data = json_file.read()
#     model = tf.keras.models.model_from_json(data)
#     model.load_weights('weight.h5')
#     tfjs.converters.save_keras_model(model, 'm')

# model = models.load_model('pneumonia_classifier_model.h5')