from threading import Thread
from termcolor import colored

import os
import subprocess

def say(text):
    os.system(f'say "{text}"')

def thread(f, args=(), daemon=False):
    """ Run a function in the background """

    t = Thread(target=f, args=args, daemon=daemon)
    t.start()

def error(text):
    print(colored(text, 'red'))

def you(text):
    print(colored(text, 'green'))

def getOutput(self, args):
    return subprocess.check_output(["spotify", "status"]).decode(sys.stdout.encoding)
