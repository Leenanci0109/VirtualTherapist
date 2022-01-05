import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib.pyplot import specgram
import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical, np_utils
from keras.layers import Input, Flatten, Dropout, Activation
from keras.layers import Conv1D, MaxPooling1D, AveragePooling1D
from keras.models import Model, model_from_json
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import confusion_matrix
from keras import regularizers
import os
import pandas as pd
import librosa
import glob
import matplotlib.pyplot as plt
import scipy.io.wavfile
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder

mylist= os.listdir(r'E:/SpeechEmotion/')

feeling_list = []
for item in mylist:
    if item[6:-16] == '02' and int(item[18:-4]) % 2 == 0:
        feeling_list.append('female_calm')
    elif item[6:-16] == '02' and int(item[18:-4]) % 2 == 1:
        feeling_list.append('male_calm')
    elif item[6:-16] == '03' and int(item[18:-4]) % 2 == 0:
        feeling_list.append('female_happy')
    elif item[6:-16] == '03' and int(item[18:-4]) % 2 == 1:
        feeling_list.append('male_happy')
    elif item[6:-16] == '04' and int(item[18:-4]) % 2 == 0:
        feeling_list.append('female_sad')
    elif item[6:-16] == '04' and int(item[18:-4]) % 2 == 1:
        feeling_list.append('male_sad')
    elif item[6:-16] == '05' and int(item[18:-4]) % 2 == 0:
        feeling_list.append('female_angry')
    elif item[6:-16] == '05' and int(item[18:-4]) % 2 == 1:
        feeling_list.append('male_angry')
    elif item[6:-16] == '06' and int(item[18:-4]) % 2 == 0:
        feeling_list.append('female_fearful')
    elif item[6:-16] == '06' and int(item[18:-4]) % 2 == 1:
        feeling_list.append('male_fearful')
    elif item[:1] == 'a':
        feeling_list.append('male_angry')
    elif item[:1] == 'f':
        feeling_list.append('male_fearful')
    elif item[:1] == 'h':
        feeling_list.append('male_happy')
    elif item[:2] == 'sa':
        feeling_list.append('male_sad')

labels = pd.DataFrame(feeling_list)
df = pd.DataFrame(columns=['feature'])
bookmark = 0
for index, y in enumerate(mylist):
    if mylist[index][6:-16] != '01' and mylist[index][6:-16] != '07' and mylist[index][6:-16] != '08' and mylist[index][
                                                                                                          :2] != 'su' and \
            mylist[index][:1] != 'n' and mylist[index][:1] != 'd':
        X, sample_rate = librosa.load('E:/SpeechEmotion/' + y, res_type='kaiser_fast', duration=2.5, sr=22050 * 2,
                                      offset=0.5)
        sample_rate = np.array(sample_rate)
        mfccs = np.mean(librosa.feature.mfcc(y=X,
                                             sr=sample_rate,
                                             n_mfcc=13),
                        axis=0)
        feature = mfccs
        # [float(i) for i in feature]
        # feature1=feature[:135]
        df.loc[bookmark] = [feature]
        bookmark = bookmark + 1

df3 = pd.DataFrame(df['feature'].values.tolist())
newdf = pd.concat([df3,labels], axis=1)
rnewdf = newdf.rename(index=str, columns={"0": "label"})
rnewdf = shuffle(newdf)
rnewdf=rnewdf.fillna(0)
newdf1 = np.random.rand(len(rnewdf)) < 0.8
train = rnewdf[newdf1]
test = rnewdf[~newdf1]
trainfeatures = train.iloc[:, :-1]
trainlabel = train.iloc[:, -1:]
testfeatures = test.iloc[:, :-1]
testlabel = test.iloc[:, -1:]

X_train = np.array(trainfeatures)
y_train = np.array(trainlabel)
X_test = np.array(testfeatures)
y_test = np.array(testlabel)
lb = LabelEncoder()

y_train = np_utils.to_categorical(lb.fit_transform(y_train))
y_test = np_utils.to_categorical(lb.fit_transform(y_test))

x_traincnn =np.expand_dims(X_train, axis=2)
x_testcnn= np.expand_dims(X_test, axis=2)


model = Sequential()

model.add(Conv1D(256, 5,padding='same',
                 input_shape=(216,1)))
model.add(Activation('relu'))
model.add(Conv1D(128, 5,padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(MaxPooling1D(pool_size=(8)))
model.add(Conv1D(128, 5,padding='same',))
model.add(Activation('relu'))
#model.add(Conv1D(128, 5,padding='same',))
#model.add(Activation('relu'))
#model.add(Conv1D(128, 5,padding='same',))

#model.add(Activation('relu'))
#model.add(Dropout(0.2))
model.add(Conv1D(128, 5,padding='same',))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(10))
model.add(Activation('softmax'))
opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)
model.summary()

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
checkpoint = ModelCheckpoint(r"E:\demo1\speeash3.h5", monitor='val_accuracy', save_weights_only=True, mode='max',
                             verbose=1,
                             save_best_only=True)
cnnhistory = model.fit(x_traincnn, y_train, batch_size=32, epochs=700, validation_data=(x_testcnn, y_test),
                       callbacks=[checkpoint])

fer_json = model.to_json()
with open("E:\demo1\speeash3.json", "w") as json_file:  # 0-62%
    json_file.write(fer_json)

