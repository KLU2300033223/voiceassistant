import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
        elif "hey shin!" in query:
            speak("Ahhaa!")
        elif "what are you doing now" in query:
            speak("I am so busy by sending lots of emails")
        elif "hey shin! Play music" in query:
            speak("yaa Now playing top songs in india")
        elif "when is your birthday" in query:
            speak("Ever day is my birthday")
        elif "call to amma" in query:
            speak("Calling amma")
        elif "had your break fast" in query:
            speak("i dont eat or drink i do like gathering information")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")
