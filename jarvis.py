import os ,sys, hashlib
import pywifi 
import time
import pyttsx3
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import socket,smtplib
import time, serial ,serialization
from geopy.geocoders import Nominatim
import string, random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
os.cpu_count()

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
        r.pause_threshold = 0
        r.energy_threshold = 10
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
    socket1 = smtplib.SMTP('smtp.gmail.com',587)
    socket1.ehlo()
    socket1.starttls()
    username = input("[+] enter your email : ")
    passwd = input("[+] enter your password : ")
    socket1.login(username,passwd)

def logingmail():
    email = input("[+] enter your email : ")
    password = input("[+] enter your password : ")
    try:
        a =socket_conn_1()
        a.socket1.sendmail(email,email,password)
        print("[+] mail sent sucessfully")
    except Exception as e:
        print(e)

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

def hashpass():
    target_hash = input("enter the hash : ")
    i =0
    while True:
        input_str = str(i).encode('utf-8')
        hashed_str = hashlib.md5(input_str).hexdigest()
        if hashed_str == target_hash:
            print("[+] hash found sucessfully")
            print("input_str",input_str.decode('utf-8'))
            print('Hash : ',hashed_str)
            break
        i += 1

def satelight_comm():
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    time.sleep(5)
    ser.write(b"AT&K0\r")
    response = ser.readline().decode('utf-8')
    print("Modem response:", response)
    ser.write(b"AT+CREG?\r")
    response = ser.readline().decode("utf-8")
    print("Modem response: ", response)
    ser.close()

def artificial_gsm():
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    time.sleep(5)
    ser.write(b"AT\r")
    resoponse = ser.readline().decode('utf-8')
    print("Modem response: " + resoponse)
    ser.write(b"AT+CMGF=1\r")
    response = ser.readline().decode('utf-8')
    print("Modem response: " + response)
    ser.write(b'"AT+CMGS="+1234567890\r')
    time.sleep(1)
    ser.write(b'this is a test message from python!\r')
    ser.write(bytes([26]))
    response = ser.readline().decode('utf-8')
    print("Modem response: " + response)
    ser.close()

def passwd_generator():
    def generate_password(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(letters) for i in range(length))
        return password

    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Your new password is:", password)

if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand().lower()
        
        if "wikipedia" in query:
            speak("[+] seraching wiki ...")
            query = query.replace("wikipedia","")
            results = wikipedia.sumary(query,sentences=2)
            speak(results)

        elif "track a location" in query:
            track_location()

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