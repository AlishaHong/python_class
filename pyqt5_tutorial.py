## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #QPushButton클래스의 객체를 생성
        #버튼의 표기 문자열을 "Quit"
        btn = QPushButton('Quit', self)
        #btn객체의 레이아웃(버튼을 창 위치의 140,70에 둔다)
        btn.move(140, 70)
        #버튼 비활성화
        btn.setDisabled(True)
        
        #버튼 사이즈
        #sizeHint는 기본사이즈를 의미함
        btn.resize(btn.sizeHint())
        #클릭 시 실행되는 것 
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   #창이 종료될 때 exit함수 실행
   sys.exit(app.exec_())