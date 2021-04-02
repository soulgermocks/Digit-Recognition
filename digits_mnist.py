# -*- coding: utf-8 -*-

import tensorflow as tf
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

mnist = tf.keras.datasets.mnist 
(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

x_train = x_train/255.0
x_test = x_test/255.0

model = tf.keras.models.Sequential([
                                   
                                    tf.keras.layers.Conv2D(28,(3,3),activation = 'relu',input_shape = (28,28,1)),
                                    tf.keras.layers.MaxPooling2D(2,2),
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128,activation='relu'),
                                    tf.keras.layers.Dense(10,activation = 'softmax')
                                    

])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10)

loss,accuracy = model.evaluate(x_test,y_test)
print(accuracy)
print(loss)
