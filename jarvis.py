import os
import pywifi 
import time
import pyttsx3
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import socket
import smtplib

from geopy.geocoders import Nominatim

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

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
    mic = sr.Microphone()
    with mic as source:
        print("[+] LISTENING ... ")
        r.pause_threshold = 1
        r.energy_threshold = 0
        audio = sr.Recognizer().listen(source)
    
    try:
        print("[+] RECOGNIZING ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"blackdevil:~ {query}\n")

    except Exception as e:
        speak("say that again please !")
        return "None"

    return query

def socket_conn_1():
    socket1 = smtplib.SMTP('smtp.google.com',587)
    socket1.ehlo()
    socket1.starttls()
    username1 = input("[+] enter your email : ")
    passwd1 = input("[+] enter your password : ")
    log1 = socket1.login(username1,passwd1)

def hrcx():
    HOST = 'localhost'
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on port {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def track_location():
    address = input("Enter address: ")

    geolocator = Nominatim(user_agent="location_tracker")
    location = geolocator.geocode(address)

    if location is not None:
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        print("Location not found.")

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
        if "wikipedia" in query:
            speak("[+] seraching wiki ...")
            query = query.replace("wikipedia","")
            results = wikipedia.sumary(query,sentences=2)
            speak(results)

        elif "hello jarvis" in query:
            speak("pleasure meeting you sir")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "bring drone to me" in query:
            socket.socket.setblocking(True)
            socket.create_connection("169.254.122.76")
        
        elif "make connection to server 1" in query:
            socket_conn_1()
        
        elif "play a music" in query:
            webbrowser.open("https://youtu.be/3iR-g-bYEYI")
        
        elif "open porn" in query:
            webbrowser.open("t.me/pornhub8756")
        
        elif"connect to server" in query:
            hrcx()
            
        elif "jarvis quit" in query:
            break