elif self.text.startswith(triggers['Play Music']):
    trigger = ""
    for y in list(triggers['Play Music']):
        if self.text.startswith(y):
            trigger = y
            break

    q = self.text[len(trigger) + 1:]
    if q == "":
        recognizer.energy_threshold = self.playing
        settings['playing'] = True
        os.system(f"spotify play")
    else:
        recognizer.energy_threshold = self.playing
        settings['playing'] = True
        os.system(f"spotify play {q}")
        time.sleep(1)

elif self.text.startswith(triggers['Pause/Resume']):
    out = utils.getOutput(['spotify', 'pause'])
    if "Pausing" in out:
        print("paused")
        settings['playing'] = False
        recognizer.energy_threshold = self.paused
    else:
        print('playing')
        settings['playing'] = True
        recognizer.energy_threshold = self.playing
