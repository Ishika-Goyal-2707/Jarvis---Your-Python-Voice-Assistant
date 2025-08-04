import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import subprocess
import re
import wikipedia
import pywhatkit

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def calculate_expression(text):
    text = text.lower()
    text = text.replace("plus", "+").replace("minus", "-")
    text = text.replace("into", "*").replace("multiplied by", "*")
    text = text.replace("divide", "/").replace("divided by", "/")
    
    try:
        result = eval(text)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't perform the calculation.")

def processCommand(command):
    command = command.lower()

    # Open YouTube
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Play song
    elif command.startswith("play"):
        try:
            song = command.replace("play", "").replace("on youtube", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
        except Exception as e:
            speak("I couldn't play the song due to an error.")
            print(f"Error playing song: {e}")

    # Google search
    elif "search for" in command:
        query = command.split("search for")[-1].strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query}")
        webbrowser.open(url)

    # Wikipedia summary
    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").strip()
        try:
            speak(f"Searching about {query}")
            summary = wikipedia.summary(query, sentences=2)
            summary = re.sub(r'\s*\([^)]*\)', '', summary)  # Remove brackets
            print(f"Wikipedia Summary: {summary}")
            speak(summary)
        except Exception as e:
            speak("Something went wrong while searching.")
            print(f"Error: {e}")

    # Calculator
    elif "calculate" in command or "solve" in command:
        expr = command.replace("calculate", "").replace("solve", "").strip()
        calculate_expression(expr)

    # Open apps
    elif "open notepad" in command:
        subprocess.Popen(["notepad.exe"])

    elif "open calculator" in command:
        subprocess.Popen(["calc.exe"])

    elif "open chrome" in command:
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        ]
        for path in chrome_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                return
        speak("Chrome is not installed.")

    elif "open vs code" in command or "open visual studio code" in command:
        try:
            subprocess.Popen(["code"])
        except FileNotFoundError:
            speak("Visual Studio Code not found.")

    elif "exit" in command or "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

    print(f"Command received: {command}")
    speak(f"You said: {command}")

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("\nRecognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")
            
            if "jarvis" in word.lower():
                speak("Yes, I'm listening.")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
