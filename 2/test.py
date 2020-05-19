from tkinter import *
import pyaudio, wave, pickle
from main import get_mfcc

class testHMM:
    def __init__(self, chunk=1024, sample_format=pyaudio.paInt16, channels=2, rate=44100, p=pyaudio.PyAudio()):
        self.CHUNK = chunk; self.FORMAT = sample_format; self.CHANNELS = channels; self.RATE = rate; self.p = p
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        self.recording = False

        #Load model train
        self.models = pickle.load(open("modelTrain.pkl", "rb"))
      
        self.main = Tk()
        self.main.geometry('330x120+500+300')
        self.main.resizable(False, False)
        self.main.title('Test HMM')
        self.record_text = Label(text="Chọn để thu")
        self.result_text = Label(text="Kết quả là ")
        self.btn_record = Button(self.main, text = "Ghi", width = 20, height = 5, command=self.record)
        self.btn_predict = Button(self.main, text = "Dự đoán", width = 20, height = 5, command=self.predict)
        self.btn_record.grid(row=1, column=0, padx = 10, pady = 10)
        self.record_text.grid(row=0, column=0)
        self.btn_predict.grid(row=1, column=1, pady = 10)
        self.result_text.grid(row=0, column=1)
        self.main.mainloop()

    def start(self):
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            self.main.update()
        stream.close()
        wf = wave.open('fileTest.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.st = 0

    def record(self):
        if self.recording == True:
            self.btn_record.config(text="Ghi")
            self.record_text.config(text="")
            self.recording = False
            self.stop()
            self.file_path = "fileTest.wav"
        elif self.recording == False:
            self.btn_record.config(text="Dừng")
            self.record_text.config(text="Đang ghi")
            self.recording = True
            self.start()

    def predict(self):
        if not self.file_path:
            print("ERROR")
            return
        O = get_mfcc(self.file_path)
        score = {cname : model.score(O, [len(O)]) for cname, model in self.models.items()}
        predict = max(score, key=score.get)
        self.result_text.config(text="Kết quả là " + predict)

test = testHMM()
