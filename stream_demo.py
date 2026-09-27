from win32com.client import Dispatch

predictions = ["A", "A", "A", "B", "B", None, "A"]

speaker = Dispatch("SAPI.SpVoice")
last_spoken = None

for letter in predictions:
    if letter is None:
        last_spoken = None
    elif letter != last_spoken:
        print("Speak:", letter)
        speaker.Speak(f"Letter {letter}")
        last_spoken = letter




