import pywifi 
import time
import pyttsx3
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import socket

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# print(voices[3].id)
engine.setProperty('voice',voices[3].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning sir")
    elif hour >= 12 and hour<= 18:
        speak("good afternoon sir")
    elif hour>= 18 and hour <21:
        speak("good evening sir")
    else:
        speak("good night sir")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("[+] LISTENING ... ")
        r.pause_threshold = 1
        r.energy_threshold = 12 
        audio = r.listen(source)
    
    try:
        speak("[+] RECOGNIZING ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"blackdevil:~ {query}\n")

    except Exception as e:
        speak("say that again please !")
        return "None"

    return query



if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
        if "wikipedia" in query:
            speak("[+] seraching wiki ...")
            query = query.replace("wikipedia","")
            results = wikipedia.sumary(query,sentences=2)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
