import speech_recognition as sr
import os
from pydub import AudioSegment

def clear(): os.system('cls' if os.name == 'nt' else 'clear')


def mp3towav():
    clear()
    src = input("Enter your mp3 file $PATH or directly name: ")
    dst = "output.wav"

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")


def main():
    mp3towav()
    r = sr.Recognizer()

    with sr.AudioFile("output.wav") as cleinkelvinn:
        audio_data = r.record(cleinkelvinn)
        text = r.recognize_google(audio_data)
        print("\n=============???=============\n" + text + "\n=============???=============")


main()
