import speech_recognition as sr
import pyttsx3
from nltk.corpus import stopwords
from textblob import Word
import pickle
import pandas as pd
import librosa
import soundfile
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
def extract_feature(sound_file, mfcc, chroma, mel):

    X = sound_file.read(dtype="float32")
    sample_rate=sound_file.samplerate
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

def load_data(test_size=0.2):
    x,y=[],[]
    for file in glob.glob(r"E:\ravdess\Actor_*\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



with open(r'E:\demo1\nspmodell4.pkl', 'rb') as fin:

    model= pickle.load(fin)

#X_new = vectorizer.transform(new_samples)
#X_new_preds = clf.predict(X_new)







# Initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s,duration=1)

    while True:
        SpeakText("How are you feeling?")
        audio = r.listen(s)
        speech = r.recognize_google(audio)
        feature = extract_feature(audio, mfcc=True, chroma=True, mel=True)
        x=[]
        x.append(feature)
        y_pre=model.predict(np.array(x))
        for i in y_pre:
            x1="Are you "+emotions[i]
            SpeakText(x1)
            print(x1)

        print('Did you say', speech)

        SpeakText(speech)
        n=input("y/n")
        if n=="n":
            break
    # Loop infinitely for user to
# speak


