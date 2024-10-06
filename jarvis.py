
import datetime
import webbrowser
import speech_recognition as sr
import win32com.client
from playsound import playsound
import subprocess
import argparse
from openai import OpenAI
from config import apikey
import os
import cv2



speaker = win32com.client.Dispatch('SAPI.SpVoice')

def ai(prompt):
    client = OpenAI(api_key=apikey)



    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content":prompt
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text1 = response.choices[0].message.content
    print(text1)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{prompt}  .txt", "w") as f:
        f.write(text1)



def speak():
    while 1:
        print("WRITE!!!")
        S = input()
        speaker.Speak(S)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speaker.speak("Good Morning sir")

    elif hour >= 12 and hour < 18:
        speaker.speak("Good Afternoon sir")

    else:
        speaker.speak("Good Evening sir")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


speaker.speak("Hello,Kapil Sir I am your A I Jarvis")

w=takeCommand()


def openwebs() :
    sites = [["youtube", "https://youtube.com"], ["stack overflow", "https://stackoverflow.com"],
             ["google", "https://google.com"]]

    for site in sites:
        if f"Open {site[0]}".lower() in w.lower():
            speaker.speak(f"opening {site[0]}  sir")
            webbrowser.open(site[1])

def playsongs():
 songs = [["sprinter", "Dave-Sprinter_(Nobadsong.com).wav"],[" Mockingbird", "Eminem-Mockingbird_(Nobadsong.com) - Copy.wav"] , ["Superman" , "Eminem-Superman_(Nobadsong.com).wav"]  , ["mathematical disrespect" , ["Lil_Mabu_-_MATHEMATICAL_DISRESPECT_arewamh.com.ng (1) - Copy.wav"] ]]
 for song in songs:
        if f"Play{song[0]}".lower() in w.lower():
            speaker.speak(f"playing{song[0]}")
            playsound(song[1])

def time():
    if"Time".lower() in w.lower():
        StrfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.speak(f"{StrfTime}")

def openapps():
     apps = [["Unity" , [r'C:\\Program Files\\Unity Hub\\unity hub.exe']]]
     for app in apps:
       if f"open{app[0]}".lower() in w.lower():
         speaker.speak(f"opening{app[0]}")
         subprocess.Popen(app[1])




def openai():
    if "use your intelligence".lower() in w.lower():
        ai(prompt=w)

if __name__ == '__main__':
 wishMe()
 while True :
  w=takeCommand()
  openai()
  openapps()
  openwebs()
  time()
  playsongs()

  