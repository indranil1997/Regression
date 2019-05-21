import tensorflow as tf
import pandas as pd
import sklearn
import io
import numpy as np
import os
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

datas = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")
input_data = datas[:,0:8]
output_data = datas[:,8]
train_x, test_x, train_y, test_y = train_test_split(input_data, output_data, test_size=0.3)
train_x = preprocessing.scale(train_x)
test_x = preprocessing.scale(test_x)

model = Sequential()
model.add(Dense(15, input_shape=(8,), kernel_initializer='uniform', activation='relu'))
model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
# model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
# model.add(Dense(10, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
model.compile(Adam(lr=0.0003), 'mean_squared_error')

earlystopper = EarlyStopping(monitor='val_loss', min_delta=0, patience=15, verbose=1, mode='auto')

history = model.fit(train_x, train_y, epochs = 6000, validation_split = 0.2, batch_size  = 10, shuffle = True, verbose = 0, callbacks = [earlystopper])

print(history.history.keys())
history_dict=history.history
loss_values = history_dict['loss']
val_loss_values=history_dict['val_loss']

plt.plot(history_dict['loss'])
plt.plot(history_dict['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()

train_y_prediction = model.predict(train_x)
test_y_prediction = model.predict(test_x)

# plt.plot(output_data)
# plt.plot(train_y_prediction,'r')
# plt.plot(test_y_prediction,'b')

# print("R2 score in training data: {:0.3f}".format(100*(r2_score(train_y, train_y_prediction))))
# print("R2 score in test data:{:0.3f}".format(100*(r2_score(test_y, test_y_prediction))))
