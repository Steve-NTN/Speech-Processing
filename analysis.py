import soundfile as sf
import sounddevice as sd
import speech_recognition as sr
import pyaudio
import time
import wave
import os


def sync_record(filename, duration, sr, channels):
    print('recording')
    my_rec = sd.rec(samplerate=sr, channels=channels, frames=int(duration*sr))
    sd.wait()
    sf.write(filename + '.wav', data=my_rec, samplerate=sr)
    print('done recording')

#pyuic5 -x "C:\Users\Administrator\Desktop\Speech Processing\display.ui" -o "C:\Users\Administrator\Desktop\Speech Processing\pp.py"
def speech():
   t = sr.AudioFile('harvard.wav')
   r = sr.Recognizer()
   with t as source:
      a = r.record(source)
   print(r.recognize_google(a))

def getText():
   f = open("Text.txt", encoding="utf8")
   listText = f.read().split("///\n")
   f.close()
   return listText

def record(data):
    f = wave.open('./wav.wav', 'wb')
    f.setframerate(8000)
    f.setsampwidth(2)
    f.setnchannels(1)
    f.writeframes(data)
    f.close()
    #return r.recognize_google(audio, language='vi-VN')
