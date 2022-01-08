import sys, os, keyboard, pyaimp, threading, time

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

## path of AIMP
path="C:/Program Files (x86)/AIMP/AIMP.exe"
try:
    client = pyaimp.Client()
    client.get_current_track_info()['title']
except:
    os.startfile(path)
    time.sleep(5)
    client = pyaimp.Client()

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout=QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setMinimumSize(300,120)
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
        self.pressing = False
        self.UiComponents()
        ##rgba(0, 120, 185, 0)
        self.setStyleSheet("background-color: black")
        self.show()

    def UiComponents(self):
        def neen():
            button.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 15px;")
            button1.setStyleSheet("background-color: rgb(0, 255, 0); border-style: none;")
        def nele():
            button.setStyleSheet("background-color: red; border-radius: 15px;")
            button1.setStyleSheet("background-color: red; border-style: none;")

        button = QPushButton("", self)
        button.setGeometry(220, 50, 60, 30)
        button.clicked.connect(self.next)
        button.setStyleSheet("background-color: rgb(255, 0, 0); border-radius: 15px;")
        button1 = QPushButton("Next", self)
        button1.setGeometry(215, 50, 50, 30)
        button1.clicked.connect(self.next)
        button1.setStyleSheet("background-color: rgb(255, 0, 0); border-style: none;")
        button.enterEvent = lambda e: neen()
        button.leaveEvent = lambda e: nele()
        button1.enterEvent = lambda e: neen()
        button1.leaveEvent = lambda e: nele()

        def pren():
            button2.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 15px;")
            button3.setStyleSheet("background-color: rgb(0, 255, 0); border-style: none;")
        def prle():
            button2.setStyleSheet("background-color: red; border-radius: 15px;")
            button3.setStyleSheet("background-color: red; border-style: none;")
    
        button2 = QPushButton("", self)
        button2.setGeometry(20, 50, 60, 30)
        button2.clicked.connect(self.previous)
        button2.setStyleSheet("background-color: red; border-radius: 15px;")
        button3 = QPushButton("Previous", self)
        button3.setGeometry(35, 50, 50, 30)
        button3.clicked.connect(self.previous)
        button3.setStyleSheet("background-color: red; border-style: none;")
        button2.enterEvent = lambda e: pren()
        button2.leaveEvent = lambda e: prle()
        button3.enterEvent = lambda e: pren()
        button3.leaveEvent = lambda e: prle()
        

        def b4sr():
            state = client.get_playback_state()
            if state == pyaimp.PlayBackState.Playing:
                button4.setText('Play')
                button4.setStyleSheet("background-color: red; border-radius: 15px;")
            elif state == pyaimp.PlayBackState.Paused:
                button4.setText('Pause')
                button4.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 15px;")
    
        state = client.get_playback_state()
        if state == pyaimp.PlayBackState.Playing:
            button4 = QPushButton("Pause", self)
            button4.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 15px;")
        else:
            button4 = QPushButton("Play", self)
            button4.setStyleSheet("background-color: red; border-radius: 15px;")
        button4.setGeometry(110, 50, 80, 30)
        button4.clicked.connect(b4sr)
        button4.clicked.connect(self.stre)

        def bt5e():
            button5.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 10;")
        def bt5l():
            button5.setStyleSheet("background-color: red; border-radius: 10;")
        
        button5 = QPushButton("+", self)
        button5.setGeometry(280, 35, 20, 20)
        button5.clicked.connect(self.open)
        button5.setStyleSheet("background-color: red; border-radius: 10;")
        button5.enterEvent = lambda e: bt5e()
        button5.leaveEvent = lambda e: bt5l()

        def bt6e():
            button6.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 10;")
        def bt6l():
            button6.setStyleSheet("background-color: red; border-radius: 10;")
    
        button6 = QPushButton("-", self)
        button6.setGeometry(0, 35, 20, 20)
        button6.clicked.connect(self.close)
        button6.setStyleSheet("background-color: red; border-radius: 10;")
        button6.enterEvent = lambda e: bt6e()
        button6.leaveEvent = lambda e: bt6l()

        label = QLabel(str(client.get_volume()), self)
        label.setGeometry(30, 84, 40, 40)
        label.setFont(QFont('Aviny', 20))
        label.setStyleSheet("color: red;")

        def vo78():
            label.setText(str(client.get_volume()))

        def bt7e():
            button7.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 7;")
        def bt7l():
            button7.setStyleSheet("background-color: red; border-radius: 7;")

        button7 = QPushButton("-", self)
        button7.setGeometry(10, 96, 15, 15)
        button7.clicked.connect(self.red)
        button7.setStyleSheet("background-color: red; border-radius: 7;")
        button7.clicked.connect(vo78)
        button7.enterEvent = lambda e: bt7e()
        button7.leaveEvent = lambda e: bt7l()

        def bt8e():
            button8.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 7;")
        def bt8l():
            button8.setStyleSheet("background-color: red; border-radius: 7;")

        button8 = QPushButton("+", self)
        button8.setGeometry(60, 96, 15, 15)
        button8.clicked.connect(self.inc)
        button8.setStyleSheet("background-color: red; border-radius: 7;")
        button8.clicked.connect(vo78)
        button8.enterEvent = lambda e: bt8e()
        button8.leaveEvent = lambda e: bt8l()

        def b9co():
            if client.is_track_repeated():
                button9.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 7;")
            else:
                button9.setStyleSheet("background-color: red; border-radius: 7;")

        button9 = QPushButton("R", self)
        button9.setGeometry(120, 96, 15, 15)
        button9.clicked.connect(self.re)
        button9.clicked.connect(b9co)
        b9co()

        def b10co():
            if client.is_shuffled():
                button10.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 7;")
            else:
                button10.setStyleSheet("background-color: red; border-radius: 7;")

        button10 = QPushButton("S", self)
        button10.setGeometry(141, 96, 15, 15)
        button10.clicked.connect(self.sh)
        button10.setStyleSheet("background-color: red; border-radius: 7;")
        button10.clicked.connect(b10co)
        b10co()

        def b11co():
            if client.is_muted():
                button11.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 7;")
            else:
                button11.setStyleSheet("background-color: red; border-radius: 7;")

        button11 = QPushButton("M", self)
        button11.setGeometry(162, 96, 15, 15)
        button11.clicked.connect(self.mu)
        button11.setStyleSheet("background-color: red; border-radius: 7;")
        button11.clicked.connect(b11co)
        button11.clicked.connect(vo78)
        b11co()

        label1 = QLabel(client.get_current_track_info()['title'], self)
        label1.setGeometry(200, 84, 100, 40)
        label1.setFont(QFont('Aviny', 15))
        label1.setStyleSheet("color: red;")

        global p
        p=1
        def update_label():
            label1.setText(client.get_current_track_info()['title'])
            time.sleep(2)
            if p==1:
                update_label()


        thr=threading.Thread(target=update_label).start()
  
    # action method
    def next(self):
        client.next()
    def previous(self):
        client.prev()
    def stre(self):
        client.play_pause()
    def open(self):
        print(client.is_track_repeated())
        os.startfile(path)
    def close(self):
        client.quit()
    def red(self):
        client.set_volume(client.get_volume()-5)
    def inc(self):
        client.set_volume(client.get_volume()+5)
    def re(self):
        if client.is_track_repeated():
            client.set_track_repeated(0)
        else:
            client.set_track_repeated(1)
    def sh(self):
        if client.is_shuffled():
            client.set_shuffled(0)
        else:
            client.set_shuffled(1)
    def mu(self):
        if client.is_muted():
            client.set_muted(0)
        else:
            client.set_muted(1)
        

class MyBar(QWidget):
    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel("Aimp Control")

        btn_size = 35

        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("background-color: red; border-style: none;")
        


        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_close)

        

        self.title.setStyleSheet("background-color: gray")
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False
        global keytos
        keytos = 0
        keyboard.on_press_key("alt", lambda _:self.keyto())

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end
            try:
                int(str(str(self.start).split(', ')[0])[-4:])
                if int(str(str(self.start).split(', ')[1])[:-1])>=870 and keyboard.is_pressed('shift'):
                    self.parent.setGeometry(980, 904, 300, 100)                    

            except:
                pass

    def keyto(self):
        global keytos
        if keytos == 0:
            self.parent.setGeometry(2980, 904, 300, 100)
            keytos = 1
        else:
            self.parent.setGeometry(980, 904, 300, 100)
            keytos = 0

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        global p
        p=0
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
