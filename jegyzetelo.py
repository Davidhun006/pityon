
import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime

r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        print("could not request results from API")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("could not play sound")
ACTIVATION_COMMAND = "hey sam"

if __name__ == "__main__":

    while True:
        a = get_audio()
        command = audio_to_text(a)

        if ACTIVATION_COMMAND in command.lower():
            print("activate")
            play_sound("What can I do for you?")

            note = get_audio()
            note = audio_to_text(note)

            if note:
                play_sound(note)

                now = datetime.now().astimezone().isoformat()
                # TODO: save your note wherever you want, e.g. in Notio
import json
import requests


class NotionClient:

    def __init__(self, token, database_id) -> None:
        self.database_id = database_id

        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }

    # read, update
    def create_page(self, description, date, status):
        create_url = 'https://api.notion.com/v1/pages'

        data = {
        "parent": { "database_id": self.database_id },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": status
                        }
                    }
                ]
            }
        }}

        data = json.dumps(data)
        res = requests.post(create_url, headers=self.headers, data=data)
        print(res.status_code)
        return res
from notion import NotionClient

token = "YOUR NOTION TOKEN HERE"
database_id = "YOUR NOTION DATABASE_ID HERE"

client = NotionClient(token, database_id)
if note:
    play_sound(note)

    now = datetime.now().astimezone().isoformat()
    res = client.create_page(note, now, status="Active")
    if res.status_code == 200:
        play_sound("Stored new item")
