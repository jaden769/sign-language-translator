import pyttsx3

engine = pyttsx3.init()

def speak_letter(letter):
    if letter == "A":
        engine.say("Letter A")
    elif letter == "B":
        engine.say("Letter B")
    elif letter == "C":
        engine.say("Letter C")
    else:
        print("Unknown letter.")
    engine.runAndWait()

if __name__=="__main__":
    letter = input("Choose A or B or C: ")
    speak_letter(letter)
