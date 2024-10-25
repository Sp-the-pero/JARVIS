import streamlit as st
import speech_recognition as sr
import os
import webbrowser
from datetime import datetime

def say(Text, Speed=175, Voice="en-uk-rp3", Pitch=0):
    os.system(f'espeak "{Text}" -s {Speed} -v {Voice} -p {Pitch}')
    st.write(f"JARVIS: {Text}")
    return Text

def voiceInput():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 2 # Waits for n seconds after the user has finished speaking
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en")
            st.write(f"User: {query}")
            return query
    except Exception as e:
        query = input("\nListening...\nUser: ")
        st.write(f"The error occured: {e}")
        # st.write(f"User: {query}")
        return query

# say("Hey! I am Jarvis. An AI Copilot, that seamlessly integrates with your web browser and OS  to boost productivity with a rich communication features. What can I do for you? it could be anything like opening the browser, or giving a link.",175, "en-uk-rp 4", 0)
# voiceInput()
say("Hi! I'm JARVIS A.I.")
while True:
    usrtext = voiceInput()
    jrtext = say(usrtext)
    
    # Website Opening
    sites = {
        "Youtube": "https://youtube.com",
        "Discord": "https://discord.com/channels/@me",
        "Whatsapp": "https://web.whatsapp.com/",
        "Upwork": "https://www.upwork.com/nx/create-profile/location",
        "GPT": "https://chat.openai.com/"
    }
    for site in sites:
        if f"Open {site}".lower()  in usrtext.lower():
            say(f"Opening {site} Mr. Stark!")
            webbrowser.open(sites[site])
    # Time Teller
    if "tell time" in usrtext.lower():
        hours = datetime.now().strftime("%I")
        mins = datetime.now().strftime("%M")
        tf = datetime.now().strftime("%p")
        say(f"Sir, Current time is {hours} hours and {mins} minutes. [{hours}:{mins}:{tf}]")
    if "open vscode" in usrtext.lower():
        say("Opening VSCode sir.")
        os.system("code") 
