import datetime
from gtts import gTTS
import random
import os
import speech_recognition as sr


def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.

    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    current_time = datetime.datetime.now().strftime("%H:%M")
    tts = gTTS(text=f"The time is {current_time}", lang=lang)
    tts.save(filename)
    print(f"The time is {current_time}. Audio saved to {filename}.")


def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.

    @params:
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!"
    ]
    joke = random.choice(jokes)
    tts = gTTS(text=joke, lang=lang)
    tts.save(audiofile)
    print(f"Joke: {joke}. Audio saved to {audiofile}.")


def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date

    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    today = datetime.datetime.now()
    day_string = today.strftime("Today is %A, %B %d, %Y.")
    tts = gTTS(text=day_string, lang=lang)
    tts.save(audiofile)
    print(f"{day_string} Audio saved to {audiofile}.")
    calendar_url = f"https://www.timeanddate.com/calendar/?year={today.year}&month={today.month}"
    return calendar_url


def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!

    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your request...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            if "time" in command:
                what_time_is_it(lang, filename)
            elif "day" in command:
                calendar_url = what_day_is_it(lang, filename)
                print(f"Check the calendar here: {calendar_url}")
            elif "joke" in command:
                tell_me_a_joke(lang, filename)
            else:
                tts = gTTS(text="Sorry, I didn't understand your request.", lang=lang)
                tts.save(filename)
                print("Request not understood. Audio saved.")
        except Exception as e:
            print(f"An error occurred: {e}")
            tts = gTTS(text="I couldn't understand you. Please try again.", lang=lang)
            tts.save(filename)
            print("Error response saved to audio.")

# Example usage:
# personal_assistant('en', 'output.mp3')
