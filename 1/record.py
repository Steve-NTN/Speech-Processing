import pyaudio
import wave
import os
import numpy  

CHUNK = 3024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
p = pyaudio.PyAudio()
frames = []
st = 1
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
def start_record():

        st = 1
        frames = []
       
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        while st == 1:
            data = stream.read(CHUNK)
            frames.append(data)

        stream.close()

        wf = wave.open('1.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

def record():
    iterator = 0
    while True:
        choose=input("Start recording? y/n? ")
        if choose=='y':
            print("recording...")
            start_record()
        if choose=='n':
            return
        iterator += 1
if __name__=='__main__':
    record()