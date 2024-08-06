import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 400)
        
        # Create layout
        vbox = QVBoxLayout()
        grid = QGridLayout()
        
        # Create display
        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; height: 50px;")
        vbox.addWidget(self.display)
        
        # Button labels
        buttons = [
            ['%', 'CE', 'C', '⌫'],
            ['1/x', 'x²', '√x', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        # Add buttons to grid
        for row, rowData in enumerate(buttons):
            for col, label in enumerate(rowData):
                button = QPushButton(label)
                button.setStyleSheet("font-size: 20px; height: 50px;")
                button.clicked.connect(self.onButtonClick)
                grid.addWidget(button, row, col)
        
        vbox.addLayout(grid)
        self.setLayout(vbox)
        
    def onButtonClick(self):
        sender = self.sender()
        text = sender.text()
        current_display = self.display.text()
        
        if text == 'C':
            self.display.setText('')
        elif text == '⌫':
            self.display.setText(current_display[:-1])
        elif text == '=':
            try:
                result = str(eval(current_display))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        elif text == 'CE':
            self.display.setText('')
        elif text == '1/x':
            try:
                result = str(1 / eval(current_display))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        elif text == 'x²':
            try:
                result = str(eval(current_display) ** 2)
                self.display.setText(result)
            except:
                self.display.setText('Error')
        elif text == '√x':
            try:
                result = str(eval(current_display) ** 0.5)
                self.display.setText(result)
            except:
                self.display.setText('Error')
        elif text == '±':
            if current_display:
                if current_display[0] == '-':
                    self.display.setText(current_display[1:])
                else:
                    self.display.setText('-' + current_display)
        else:
            self.display.setText(current_display + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())