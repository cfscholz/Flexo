import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

class ScreenOne(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Add gif
        self.gif = QLabel(self)
        self.gif.setPixmap(QPixmap("gifs/ring.gif"))
        self.gif.setGeometry(133, 827, 300, 300)

        # Add text "1"
        self.text_1 = QLabel("1", self)
        self.text_1.setGeometry(298, 946, 300, 300)
        self.text_1.setStyleSheet("QLabel {color: white; font: inter bold 170px;}")

        # Add text "in motion"
        self.text_2 = QLabel("in motion", self)
        self.text_2.setGeometry(570, 921, 300, 300)
        self.text_2.setStyleSheet("QLabel {color: white; font: inter bold 170px;}")

class ScreenTwo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Add text "OK"
        self.text = QLabel("OK", self)
        self.text.setGeometry(642, 921, 300, 300)
        self.text.setStyleSheet("QLabel {color: white; font: inter bold 170px;}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1536, 2048)

        self.screen_one = ScreenOne(self)
        self.screen_two = ScreenTwo(self)

        self.switch_to_screen_one()

    def switch_to_screen_one(self, *args):
        self.setCentralWidget(self.screen_one)

    def switch_to_screen_two(self, *args):
        self.setCentralWidget(self.screen_two)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
