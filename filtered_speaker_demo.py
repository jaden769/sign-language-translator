from win32com.client import Dispatch

from stability_filter import filter_stable_predictions


if __name__ == "__main__":
    predictions = ["A", "A", "A", "C", "B", "B", "B", None, "A", "A", "A"]
    accepted = filter_stable_predictions(predictions)

    speaker = Dispatch("SAPI.SpVoice")

    for letter in accepted:
        print("Speaking:", letter)
        speaker.Speak(f"Letter, {letter}")