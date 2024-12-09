import os
import sys
import hashlib
import pywifi
import time
import pyttsx3
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import socket
import smtplib
import serial
import string
import random
from geopy.geocoders import Nominatim
import psutil
import pygetwindow as gw

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning sir")
    elif hour < 18:
        speak("Good afternoon sir")
    elif hour < 21:
        speak("Good evening sir")
    else:
        speak("Good night sir")

def takecommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("[+] Listening ...")
        r.pause_threshold = 0.7
        r.energy_threshold = 300
        audio = r.listen(source)
    
    try:
        print("[+] Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"blackdevil:~ {query}\n")
    except Exception as e:
        speak("Say that again please!")
        return "None"

    return query.lower()

def socket_conn_1():
    try:
        socket1 = smtplib.SMTP('smtp.gmail.com', 587)
        socket1.ehlo()
        socket1.starttls()
        username = input("[+] Enter your email: ")
        passwd = input("[+] Enter your password: ")
        socket1.login(username, passwd)
        print("[+] Logged in successfully.")
        return socket1
    except Exception as e:
        print(f"Error: {e}")
        return None

def logingmail():
    try:
        email = input("[+] Enter your email: ")
        password = input("[+] Enter your password: ")
        socket1 = socket_conn_1()
        if socket1:
            socket1.sendmail(email, email, password)
            print("[+] Mail sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

def hrcx():
    try:
        HOST = 'localhost'
        PORT = 8000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            speak(f"Server listening on port {PORT}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
    except Exception as e:
        print(f"Error: {e}")

def track_location():
    address = input("Enter address: ")
    geolocator = Nominatim(user_agent="location_tracker")
    location = geolocator.geocode(address)

    if location:
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        print("Location not found.")

def hashpass():
    target_hash = input("Enter the hash: ")
    i = 0
    while True:
        input_str = str(i).encode('utf-8')
        hashed_str = hashlib.md5(input_str).hexdigest()
        if hashed_str == target_hash:
            print("[+] Hash found successfully")
            print("Input string:", input_str.decode('utf-8'))
            print('Hash:', hashed_str)
            break
        i += 1

def satelight_comm():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        time.sleep(5)
        ser.write(b"AT&K0\r")
        response = ser.readline().decode('utf-8')
        print("Modem response:", response)
        ser.write(b"AT+CREG?\r")
        response = ser.readline().decode("utf-8")
        print("Modem response:", response)
        ser.close()
    except Exception as e:
        print(f"Error: {e}")

def artificial_gsm():
    try:
        ser = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
        time.sleep(5)
        ser.write(b"AT\r")
        response = ser.readline().decode('utf-8')
        print("Modem response:", response)
        ser.write(b"AT+CMGF=1\r")
        response = ser.readline().decode('utf-8')
        print("Modem response:", response)
        ser.write(b'AT+CMGS="+1234567890"\r')
        time.sleep(1)
        ser.write(b'This is a test message from Python!\r')
        ser.write(bytes([26]))
        response = ser.readline().decode('utf-8')
        print("Modem response:", response)
        ser.close()
    except Exception as e:
        print(f"Error: {e}")

def passwd_generator():
    def generate_password(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(letters) for i in range(length))
        return password

    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Your new password is:", password)

def get_current_activity():
    # Get the active window title
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return active_window.title
    return "No active window"

def suggest_based_on_activity(activity):
    if "Google Chrome" in activity or "Mozilla Firefox" in activity:
        speak("I see you are browsing the web. Would you like me to find some interesting articles for you?")
    elif "Microsoft Word" in activity:
        speak("It looks like you are working on a document. Would you like me to suggest some templates?")
    elif "Visual Studio Code" in activity:
        speak("I see you are coding. Would you like me to look up some documentation for you?")
    else:
        speak("I am not sure what you are doing, but let me know if you need assistance!")

if __name__ == "__main__":
    wishme()
    speak("Starting voice recognition module")

    while True:
        query = takecommand()
        
        # Check current activity and suggest
        current_activity = get_current_activity()
        suggest_based_on_activity(current_activity)

        if "wikipedia" in query:
            speak("[+] Searching Wikipedia ...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif "track a location" in query:
            track_location()

        elif "hello jarvis" in query:
            speak("Pleasure meeting you sir")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "bring drone to me" in query:
            speak("This command is not implemented.")

        elif "make connection to server 1" in query:
            socket_conn_1()
        
        elif "play a music" in query:
            webbrowser.open("https://youtu.be/3iR-g-bYEYI")
        
        elif "connect to server" in query:
            hrcx()
            
        elif "jarvis quit" in query:
            speak("Goodbye, sir!")
            break
