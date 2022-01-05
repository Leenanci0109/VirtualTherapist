import speech_recognition as sr
import pyttsx3
from nltk.corpus import stopwords
from textblob import Word
import pickle
import pandas as pd


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



with open(r'E:\demo1\smodel2.pkl', 'rb') as fin:

    vectorizer, clf = pickle.load(fin)

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
        s1=[]
        s1.append(speech)
        speech1=pd.DataFrame(s1)
        speech1[0] = speech1[0].str.replace('[^\w\s]', ' ')

        stop = stopwords.words('english')
        speech1[0] = speech1[0].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

        speech1[0] = speech1[0].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
        # Extracting Count Vectors feature from our tweets
        tweet_count = vectorizer.transform(speech1[0])
        # Predicting the emotion of the tweet using our already trained linear SVM
        tweet_pred = clf.predict(tweet_count)
        for i in tweet_pred:
            if i==2:
                SpeakText("Are you sad? ")
                print("Are you sad? ")
            elif i==1:
                SpeakText("Are you happy?")
                print("Are you happy?")

        print('Did you say', speech)

        SpeakText(speech)
        n=input("y/n")
        if n=="n":
            break
    # Loop infinitely for user to
# speak


