from termcolor import colored
from queue import Queue

import speech_recognition as sr
import utils

recognizer = sr.Recognizer()
mic = sr.Microphone()
audio_queue = Queue()

# Modify default recognizer values
config = utils.config()
recognizer.pause_threshold = config['pause_threshold']
recognizer.energy_threshold = config['energy_threshold']['value']
recognizer.dynamic_energy_threshold = config['dynamic_energy_threshold']

class Process:
    def __init__(self, text):
        self.text = text

    def start(self):
        """ Do some fancy if statements shit

        Example :
        if self.text.startswith(("hey", "hi")):
            utils.say("hello world") """

        pass

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
    print("Started listen thread")
    while True:
        config = utils.config()
        if config['energy_threshold']['adjust_for_ambient_noise'] == True:
            recognizer.adjust_for_ambient_noise(source)

        if config['print_threshold'] == True:
            print(recognizer.energy_threshold)

        audio_queue.put(recognizer.listen(source))
