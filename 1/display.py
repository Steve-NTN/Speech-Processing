# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from analysis import getText, getSentences, getTitle
import pyaudio
import wave
import os
listText = getText()
indexText = 0; indexSen = 0

topic =  ['thoi su', 'goc nhin','the gioi', 
            'kinh doanh', 'giai tri', 'the thao', 
            'phap luat', 'giao duc', 'suc khoe', 
            'doi song', 'du lich', 'khoa hoc', 
            'so hoa', 'xe', 'y kien', 'tam su']

class Ui_MainWindow(object):
    st = 1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.CHUNK = 3024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(180, 60, 691, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 480, 61, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 480, 61, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 29, 30, 33))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setIcon(QtGui.QIcon('./cf.png'))
        self.pushButton_5.setIconSize(QtCore.QSize(25,25))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(25, 110, 131, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Please enter a name")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 300, 141, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 470, 91, 51))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setAcceptDrops(False)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(710, 30, 161, 31))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        for t in getTitle():
            self.comboBox.addItem(t)

        self.listWidget.addItem(getSentences(listText[0])[0])
        self.lineEdit_2.setText("1/{}".format(len(getSentences(listText[0]))))
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.start_record)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_5.clicked.connect(self.title)

   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Record"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "<<"))
        self.pushButton_4.setText(_translate("MainWindow", ">>"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))

    def title(self):
        global indexText
        global indexSen
        for i in range(len(getTitle())):
            if self.comboBox.currentText() == getTitle()[i]:
                self.listWidget.clear()
                self.listWidget.addItem(getSentences(listText[i])[0])
                indexText = i; indexSen = 0
                self.lineEdit.clear()
                self.lineEdit.setText(str(indexSen+1))
                self.getIndex()

    def check(self, p):
        if p in range(len(getSentences(listText[indexText]))):
            return True
        return False
    
    def back(self):
        global indexText
        global indexSen
        if self.check(indexSen-1):
            self.listWidget.clear()
            self.listWidget.addItem(getSentences(listText[indexText])[indexSen - 1])
            indexSen -= 1
            self.lineEdit.clear()
            self.lineEdit.setText(str(indexSen+1))
            self.getIndex()
        

    def next(self):
        global indexText
        global indexSen
        if self.check(indexSen + 1):
            self.listWidget.clear()
            self.listWidget.addItem(getSentences(listText[indexText])[indexSen + 1])
            indexSen += 1
            self.lineEdit.clear()
            self.lineEdit.setText(str(indexSen+1))
            self.getIndex()

    def getIndex(self):
        global indexSen
        self.lineEdit_2.clear()
        string = "{}/{}".format(indexSen + 1, len(getSentences(listText[indexText])))
        self.lineEdit_2.setText(string)

    # def start(self): 
    #     self.st = False 
    #     fileName = str(self.lineEdit.text())
    #     if fileName != "":
    #         sync_record(fileName, 5, 22050, 1)
    #     while self.st == False:
    #         QtCore.QCoreApplication.processEvents()
    #     self.lineEdit.clear()
        
    def start_record(self):

        self.st = 1
        self.frames = []
        fileName = str(self.lineEdit.text())
        if fileName != "":
            stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
            while self.st == 1:
                data = stream.read(self.CHUNK)
                self.frames.append(data)
                QtCore.QCoreApplication.processEvents()

            stream.close()

            wf = wave.open('./data/{}/{}.wav'.format(topic[indexText], fileName), 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()

    def stop(self):
        
        self.st = 0

    def browse(self):    
        path = os.path.realpath("C:/Users/Administrator/Desktop/Speech Processing/1/data")
        os.startfile(path)
        print(path)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
