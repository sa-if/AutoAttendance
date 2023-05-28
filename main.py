import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice of the text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Listen to the microphone input and respond with "yes sir" if it detects the word "david"
with sr.Microphone() as source:
    print("Listening...")
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            if "david" in text.lower():
                engine.say("Yes sir")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
