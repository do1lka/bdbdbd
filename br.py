from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime

app = QApplication([])

class frs_window(QWidget):#первое окно
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('окно 1')
        self.resize(1920, 1080)
    #скрытие первого окна
    def dasd(self):
        self.hide()
        second_window.show()
    def unitUI(self):
        self.label1 = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
        self.label2 = QLabel('Тест Руфье: тут крч текст много букаф мне лень его печатать')
        self.button1 = QPushButton('Начать')
        self.v_line1 = QVBoxLayout()
        self.v_line1.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.v_line1.addWidget(self.label2, alignment=Qt.AlignCenter)
        self.v_line1.addWidget(self.button1, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line1)
    def connects(self):
        self.button1.clicked.connect(self.dasd)
class sec_window(QWidget):#второе окно
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()
        self.connects()
    def set_appear(self):
        self.setWindowTitle('окно 2')
        self.resize(1920, 1080)
    def dasd2(self):
        self.hide()
        third_window.show()
    def unitUI(self): 
        self.label3 = QLabel('Текст1')
        self.line_edit1 = QLineEdit()
        self.label4 = QLabel('Текст2')
        self.line_edit2 = QLineEdit()
        self.label5 = QLabel('Текст3')
        self.button2 = QPushButton('Таймер 1')
        self.line_edit3 = QLineEdit()
        self.label6 = QLabel('Текст4')
        self.button3 = QPushButton('Таймер2')
        self.label7 = QLabel('Текст5')
        self.button4 = QPushButton('Таймер3')
        self.line_edit4 = QLineEdit()
        self.line_edit5 = QLineEdit()
        self.button5 = QPushButton('След. окно')
        self.label_timer = QLabel('Тут время')
        self.v_line2 = QVBoxLayout()
        self.v_line2.addWidget(self.label3, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.line_edit1, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.label4, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.line_edit2, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.label5, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.button2, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.line_edit3, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.label6, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.button3, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.label7, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.line_edit4, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.line_edit5, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.button4, alignment=Qt.AlignLeft)
        self.v_line2.addWidget(self.button5, alignment=Qt.AlignCenter)
        self.v_line3 = QVBoxLayout()
        self.v_line3.addWidget(self.label_timer, alignment=Qt.AlignCenter)
        self.h_line = QHBoxLayout()
        self.h_line.addLayout(self.v_line2)
        self.h_line.addLayout(self.v_line3)
        self.setLayout(self.h_line)
    def connects(self):
        self.button2.clicked.connect(self.timer1)
        self.button3.clicked.connect(self.timer2)
        self.button4.clicked.connect(self.timer3)
        self.button5.clicked.connect(self.dasd2)
    #таймер 1
    def timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent)
        self.timer.start(1000)

    def timeEvent(self):
        global time
        time = time.addSecs(-1)
        self.label_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent2)
        self.timer.start(2000)

    def timeEvent2(self):
        global time
        time = time.addSecs(-1)
        self.label_timer.setText(time.toString('hh:mm:ss')[6:8])
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent)
        self.timer.start(1000)

    def timeEvent3(self):
        global time
        time = time.addSecs(-1)
        self.label_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') <= '00:00:59':
            self.label_timer.setStyleSheet("color: rgb (0, 255, 0)")
        if time.toString('hh:mm:ss') <= '00:00:45':
            self.label_timer.setStyleSheet("color: rgb (0, 0, 0)")
        if time.toString('hh:mm:ss') <= '00:00:15':
            self.label_timer.setStyleSheet("color: rgb (0, 255, 0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
class thr_window(QWidget):#третье окно
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
    def set_appear(self):
        self.setWindowTitle('окно 3')
        self.resize(1920, 1080)

first_window = frs_window()
second_window = sec_window()
third_window = thr_window()
app.exec_()
