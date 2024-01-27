import speech_recognition as sr 

def take_command():
    r = sr.Recognizer()
    source = sr.Microphone()  # Create an instance of the Microphone class
    with source as audio_source:  # Use the instance in the with block
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(audio_source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
    except Exception as e:
        print(e)
        return ""

    return query