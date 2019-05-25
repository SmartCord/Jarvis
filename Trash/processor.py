import json
import utils
import datetime

settings = "settings.json"

def modifySettings(key, newvalue):
    with open(settings) as f:
        r = json.load(f)
        f.close()

    r[key] = newvalue

    with open(settings, 'w+') as f:
        f.seek(0)
        json.dump(r, f, indent=4)
        f.close()

class Process:
    def __init__(self, text):
        self.text = text
        self.paused = 1000
        self.playing = 190000

    def toPlaying(self):
        modifySettings('energy_threshold', {'custom':True, 'value':self.playing})

    def toPaused(self,custom=False):
        modifySettings('energy_threshold', {'custom':custom, 'value':self.paused})

    def start(self):
        triggers = ("what time is it", "time check")
        if self.text.startswith(triggers):
            x = datetime.datetime.now().strftime("%I:%M %p")

            self.toPlaying()
            utils.say(f"It is currently {x}")
            self.toPaused(True)
