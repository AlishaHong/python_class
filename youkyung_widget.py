import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import datetime



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        #버튼만들기
        btn1 = QPushButton('클릭해봥',self)
        btn2 = QPushButton('현재시각',self)
        
        btn2.setStyleSheet("white")

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        
        font1 = self.label.font()
        font1.setBold(True)
        self.label.setFont(font1)

        
        
        #버튼을 클릭했을때 연결된 함수 
        btn1.clicked.connect(self.myNumber)
        btn2.clicked.connect(self.button2)
        
        
        #레이아웃 정하기
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.setWindowTitle("YouKyung")
        self.setGeometry(300,300,300,300)
        self.show()
    
    
    # 텍스트 입력은 lineedit로 받기 
    def myNumber(self):
        self.numberList = []
        a = int(input())
        while len(self.numberList) < 7 :
            self.numberList.append(a)
            return self.numberList
        
    def button1(self,numberList):
        self.label.setText(self.numberList)
    
    
    def button2(self,label1):
        current_datetime = datetime.datetime.now()
        self.label.setText(f'Current Time: {current_datetime.strftime("%Y-%m-%d %H:%M:%S")}')
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
