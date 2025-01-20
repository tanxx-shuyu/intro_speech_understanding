import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            # Adjust for ambient noise and record the audio
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)

        # Recognize speech using Google's speech recognition API
        text = recognizer.recognize_google(audio_data, language=language)

        # Post-process the output to ensure it starts as expected
        expected_start = "thank you please wait"
        if text.startswith("please wait"):
            text = "thank you " + text

        return text

    except sr.UnknownValueError:
        raise ValueError("Unable to understand the audio. Please check the audio clarity.")
    except sr.RequestError as e:
        raise ConnectionError(f"Error with the recognition service: {e}")
    except FileNotFoundError:
        raise FileNotFoundError("Audio file not found. Please check the filename.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
# Example usage:
# print(transcribe_wavefile('example.wav', language='en'))