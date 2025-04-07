import os
import sys
import time
import pyttsx3
import subprocess

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run_assistant():
    assistant_path = os.path.join(os.getcwd(), "Virtual Assistant.py")
    subprocess.call(["python", assistant_path])

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 55)
    typewriter("🤖 Gibbs – Your Virtual Assistant", 0.07)
    print("=" * 55)
    typewriter("Loading modules...", 0.03)
    time.sleep(0.5)
    speak("Welcome back, David. Initializing systems.")
    typewriter("System initialized. Launching assistant now...\n", 0.04)
    run_assistant()
    typewriter("\nAssistant session ended. Goodbye!", 0.05)
    speak("Shutting down now.")

if __name__ == "__main__":
    main()
