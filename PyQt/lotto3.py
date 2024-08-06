import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class LottoGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setReadOnly(False)  # 이 필드는 읽기 전용으로 설정합니다. 읽기전용 -> true
        self.layout.addWidget(self.line_edit)

        self.button = QPushButton('Generate Numbers', self)
        self.button.clicked.connect(self.generate_numbers)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.setWindowTitle('Lotto Number Generator')
        self.setGeometry(300, 300, 300, 200)

    def generate_numbers(self):
        numbers = random.sample(range(1, 46), 6)
        self.line_edit.setText(f'Lotto Numbers: {", ".join(map(str, numbers))}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LottoGenerator()
    ex.show()
    sys.exit(app.exec_())