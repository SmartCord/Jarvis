from threading import Thread
from termcolor import colored

import os
import subprocess
import sys
import json

def say(text):
    os.system(f'say "{text}"')

def thread(f, args=(), daemon=False):
    """ Run a function in the background """

    t = Thread(target=f, args=args, daemon=daemon)
    t.start()

def config():
    with open("config.json") as f:
        r = json.load(f)
    return r

def error(text):
    print(colored(text, 'red'))

def you(text):
    print(colored(text, 'green'))

def getOutput(self, args):
    return subprocess.check_output(args).decode(sys.stdout.encoding)
