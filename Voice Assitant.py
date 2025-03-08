import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import os
import sys

def take_command():
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
        print("Say that again please...")
        return "None"
    return query


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#speed control
#rate = engine.getProperty('rate')
#engine.setProperty('rate',150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. How can I help you today?")

def execute_task(query):
    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")
    elif 'open google' in query.lower():
        webbrowser.open("google.com")
    #elif 'open e-mail' in query.lower():
     #   webbrowser.open("gmail.com")
    elif 'open linkedin' in query.lower():
        webbrowser.open("https://www.linkedin.com/in/ankur-singh-6b3422281/")
    elif 'open github' in query.lower():
        webbrowser.open("https://github.com/Asingh108")
    elif 'play music' in query.lower():
        music_dir = 'path_to_your_music_directory'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'jokes' in query.lower():
        joke = pyjokes.get_joke('en','neutral')
        print(joke)
        speak(f"Sir, here the joke {joke}, Hope you like it.")
    elif 'thank you' in query.lower():
        speak("It's my pleasure sir")
    elif 'turn off' in query.lower():
        speak("Terminate!")
        sys.exit()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        if query == "none":
            continue
        execute_task(query)
