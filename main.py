import os
import pygame
import pyautogui
import pywhatkit
import speech_recognition as sr
from scrapper.bot_scrapper import *
from datetime import datetime
from gpt4 import *
from functions.emailsender import *

# en-AU-WilliamNeural
# en-CA-ClaraNeural
# en-CA-LiamNeural

sleep_mode = False

def speak(text):
    voice = "en-AU-WilliamNeural"
    command = (
        f'edge-tts --voice "{voice}" --text "{text}" --write-media "audio/output.mp3"'
    )
    os.system(command)

    pygame.init()

    pygame.mixer.init()

    try:
        pygame.mixer.music.load("audio/output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def take_command():
    r = sr.Recognizer()
    source = sr.Microphone()  # Create an instance of the Microphone class
    with source as audio_source:  # Use the instance in the with block
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(audio_source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
    except Exception as e:
        print(e)
        return ""

    return query


click_on_chat_button()
while True:
    query = take_command().lower()
    print("\n You:" + query)
    if "open" in query:
        app_name = query.replace("open", "")
        speak("opening" + app_name)
        pyautogui.press("super")
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.7)
        pyautogui.press("enter")

    elif "switch tab" in query:
            pyautogui.hotkey('ctrl','tab')
        
    elif "close tab" in query:
            pyautogui.hotkey('ctrl','w')
    elif "close" in query:
        pyautogui.hotkey("alt", "f4")
        speak("Done Sir!")

    elif "play" in query:
        song_name = query.replace("play", "")
        speak("Sure Sir. Playing" + song_name + "in youtube")
        pywhatkit.playonyt(song_name)
    
    elif "time" in query:
        current_time = datetime.now().strftime('%H:%M %p')
        speak('Current time is ' + current_time)
        
    elif "sleep" in query:
        speak('Ok sir , I am going to sleep but you can call me any time just say wake up and I will be  there for you.')
        
    elif "write an email" in query or "compose an email" in query or "send an email" in query:
        speak('Sure sir, Can you provide me the name of the user to whom you want to send email below: ')
        recever = input('Enter his/her email address: ')
        speak ('What should be the subject of the email')
        subject = take_command()
        speak ('What should be the content of the email. Just provide me the prompt')
        email_prompt = take_command()
        content = GPT('write me a email for' + email_prompt)
        send_email(recever, subject, content)
        speak(f'Done Sir. Email sent successfully  to {recever}')
        
    else:
        sendQuery(query)
        isBubbleLoaderVisible()
        response = retriveData()
        speak(response)

    while sleep_mode:
        query = take_command().lower()
        print(query)
        if "wake up" in query:
            speak('I am awake now, How can I help you sir ?')
            sleep_mode = False
            

# https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Chat%20with%20Virtual%20Assistant%20Liam%22%2C%22botConversationDescription%22%3A%22Liam%20is%20Virtual%20Assistant%20%22%2C%22botId%22%3A%22e965b39f-c840-4ac4-b043-3730131b8b5a%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%22e965b39f-c840-4ac4-b043-3730131b8b5a%22%2C%22webhookId%22%3A%2217e7063b-a334-4127-9911-7fdb3af46e1f%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22botName%22%3A%22Virtual%20Assistant%20Liam%22%2C%22stylesheet%22%3A%22https%3A%2F%2Fwebchat-styler-css.botpress.app%2Fprod%2Fe5e48362-8e20-4dd8-87d2-b97d2ef10930%2Fv50631%2Fstyle.css%22%2C%22frontendVersion%22%3A%22v1%22%2C%22showBotInfoPage%22%3Atrue%2C%22showPoweredBy%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%229gi3M9rCtq0ZSucoFyk7oJ2c17GzqzQS%22%7D%7D
