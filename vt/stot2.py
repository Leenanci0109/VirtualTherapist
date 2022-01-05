import speech_recognition as sr
import pyttsx3
import recaud
from nltk.corpus import stopwords
from textblob import Word
import pickle
import pandas as pd
import librosa
import soundfile as sf
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}
#DataFlair - Emotions to observe
observed_emotions=['happy', 'sad','angry', 'disgust']
print(emotions['02'])

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def extract_feature(sound_file, mfcc, chroma, mel):
    X, sample_rate = sf.read(sound_file)
    #X = sound_file.read(dtype="float32")
    #sample_rate=sound_file.samplerate
    if chroma:
        stft=np.abs(librosa.stft(X))
        result=np.array([])
    if mfcc:
        mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result=np.hstack((result, mfccs))
    if chroma:
        chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
        result=np.hstack((result, chroma))
    if mel:
        mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
        result=np.hstack((result, mel))
    return result



with open(r'E:\demo1\nspmodell4.pkl', 'rb') as fin:

    model= pickle.load(fin)

#X_new = vectorizer.transform(new_samples)
#X_new_preds = clf.predict(X_new)







# Initialize the recognizer

while True:
    SpeakText("How are you feeling?")
    #audio = os.path.basename(r"E:\demo1\output.wav")
    #audio=golb(r"E:\demo1\output.wav",'r')
    #recaud.recaudio()
    feature = extract_feature(r"E:\demo1\output.wav", mfcc=True, chroma=True, mel=True)
    x = []
    x.append(feature)
    y_pre = model.predict(np.array(x))
    for i in y_pre:
        x1 = "Are you " + str(i)
        SpeakText(x1)
        print(x1)
    n = input("y/n:")
    if n == "n":
        break

    # Loop infinitely for user to
# speak


