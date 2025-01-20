import gtts

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTs(text=text, lang=lang) to synthesize speech, then write it to filename.

    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    try:
        # Create a gTTS object
        tts = gtts.gTTS(text=text, lang=lang)

        # Save the synthesized speech to the given filename
        tts.save(filename)
        print(f"Speech synthesized and saved to {filename}")

    except ValueError as ve:
        raise ValueError(f"Invalid parameters for synthesis: {ve}")
    except Exception as e:
        raise RuntimeError(f"An error occurred during speech synthesis: {e}")

# Example usage:
# try:
#     synthesize("Hello, world!", "en", "output.mp3")
# except Exception as e:
#     print(f"Error: {e}")
