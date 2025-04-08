import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 GUI Example")
        self.setGeometry(100, 100, 300, 200)

        # 레이아웃과 위젯들 생성
        self.layout = QVBoxLayout()

        self.label = QLabel("")  # 초기에는 아무 텍스트 없음
        self.button = QPushButton("Say Hello")

        # 버튼 클릭 시 함수 연결
        self.button.clicked.connect(self.say_hello)

        # 위젯들을 레이아웃에 추가
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # 레이아웃을 이 위젯(창)에 설정
        self.setLayout(self.layout)

    def say_hello(self):
        self.label.setText("Hello, World!")

# 앱 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = HelloWorldApp()
    window.show()

    sys.exit(app.exec())
