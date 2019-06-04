# Support Ended
As of June 4 2019 support for Jarvis has ended. Please check out (Jarvis V2)[https://github.com/SmartCord/Jarvis-V2] for a much better and easier to use voice assistant

# Jarvis
Jarvis is a simple input and output voice assistant framework.

# How to use it?
First you have to clone the repository by doing `git clone https://github.com/SmartCord/Jarvis` then cd to the directory by doing `cd Jarvis`.

### Installing the requirements
```
pip install -r requirements.txt
```
After installing the requirements you can start configuring it
### Configuring
Rename `template.py` to your voice assistant name e.g, `jarvis.py`, `coolAssistant.py`

#### config.json
```
{
    "energy_threshold": {
        "adjust_for_ambient_noise": true,
        "value": 800
    },
    "pause_threshold": 0.5,
    "dynamic_energy_threshold": true,
    "print_threshold": false
}

```
|Key  |Default Value  |Description    |
|--|--|-- |
| energy_threshold.adjust_for_ambient_noise |true  | Automatically adjust energy_threshold value based on ambient noise.  |
| energy_threshold.value |800  | Represents the energy level threshold for sounds. Values below this threshold are considered silence, and values above this threshold are considered speech. Will be ignored if adjust_for_ambient_noise is true |
| pause_threshold |0.5  | Represents the minimum length of silence (in seconds) that will register as the end of a phrase.|
| dynamic_energy_threshold |true  | Represents whether the energy level threshold for sounds should be automatically adjusted based on the currently ambient noise level while listening.|
| print_threshold |false  | Prints out the current threshold. Useful for debugging |

### Adding commands
Adding commands is a simple process. All you have to do is add an if/elif statement for every command in the start function of the Process class in `template.py`

#### Variables
|Variable|Description  |
|--|--|
| self.text |The words you said converted into text  |


#### Example
```
class Process:
    def __init__(self, text):
        self.text = text

    def start(self):
        if self.text == "what time is it":
            x = datetime.datetime.now().strftime("%I:%M %p") # This assumes you have the datetime module imported
            utils.say(f"It is currently {x}")
```
If you say `what time is it` the assistant will reply with `It is currently <whatever time is it> <pm|am>`
