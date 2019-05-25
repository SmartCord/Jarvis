from termcolor import colored
from queue import Queue

import speech_recognition as sr
import time
import utils
import json
import os
import datetime
import sys
import subprocess
import pyaudio
import struct
import math
import webbrowser

recognizer = sr.Recognizer()
mic = sr.Microphone()
audio_queue = Queue()

# Modify default recognizer values
recognizer.pause_threshold = 0.5
recognizer.energy_threshold = 5000
recognizer.dynamic_energy_threshold = False

class Process:
    def __init__(self, text):
        self.text = text
        self.paused = 1500
        self.playing = 2100
        self.triggers = {
            "Time Check": ("what time is it", "time check"),
            "Open Website": ("open", "please", "can you open", "google", "please google", "can you google")
        }

    def start(self):
        triggers = self.triggers
        if self.text.startswith(triggers['Time Check']):
            x = datetime.datetime.now().strftime("%I:%M %p")

            recognizer.energy_threshold = self.playing
            utils.say(f"It is currently {x}")
            recognizer.energy_threshold = self.paused

        elif self.text.startswith(triggers['Open Website']):

            with open("sites.json") as f:
                sites = json.load(f)

            trigger = ""
            for y in list(triggers['Open Website']):
                if self.text.startswith(y):
                    trigger = y
                    break

            q = self.text[len(trigger) + 1:]
            if q.endswith(("in a new tab", "ina new tab", "in the new tab")):
                _type = 0
            elif q.endswith(("in a new window", "ina new window", "in the new window")):
                _type = 1
            else:
                _type = 0
            q = q.replace(" in a new tab", "").replace(" ina new tab", "").replace(" in a new window", "").replace(" ina new window", "").replace("in the new window", "").replace("in the new tab", "")
            try:
                site = sites[q]
            except KeyError:
                if q.endswith((".com", "dotcom", "dot com", "that com", "thatcom")):
                    site = f"http://{q}"
                else:
                    site = f"http://google.com/search?q={q}"

            if _type == 0:
                webbrowser.open_new_tab(site)
            elif _type == 1:
                webbrowser.open_new(site)

def process():
    """ Try to recognize what you just said """
    print("Started Recognize Thread")
    while True:
        source = audio_queue.get()
        if source is None: break

        try:
            print(colored("Recognizing", "yellow"))
            value = recognizer.recognize_google(source)
            utils.you(f"You said : {value}")
            yes = Process(value)
            yes.start()
        except sr.UnknownValueError:
            pass
        except Exception as e:
            utils.error(f"Error on process function : {e}")

        audio_queue.task_done()


# List of functions to run in the background
threadTargets = [
    [process, (), True]
]

for target in threadTargets:
    utils.thread(target[0], args=target[1], daemon=target[2])

""" Keep listening and once it hears something process the
source using process(source) in the background and start listening again """

with mic as source:
    print("Started listening thread")
    while True:
        audio_queue.put(recognizer.listen(source))
