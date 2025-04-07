import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import random

myname = "Gibbs"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning, David")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, David")
    else:
        speak("Good Evening, David")
    speak("I am Gibbs, How may I help you?")

def hearMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query
    except Exception:
        print("Say that again, please")
        return None

def main():
    wishMe()
    while True:
        query = hearMe()
        if query is None:
            continue
        query = query.lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("Your query was too broad. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find anything for that.")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\david\\Music"
            songs = os.listdir(music_dir)
            if songs:
                song = os.path.join(music_dir, random.choice(songs))
                speak("Playing music...")
                os.startfile(song)
            else:
                speak("No music files found.")

        elif "what is your name" in query:
            speak("I am Gibbs, your virtual assistant")

        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye, David.")
            break

        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
