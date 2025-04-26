from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar
from my_widget import MainWidget

import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainWidget(self)
        self.setWindowTitle("My Custom tab Widget")
        self.resize(1080, 720)

        self.set_status_bar()

        self.setCentralWidget(self.main_widget)

    def set_status_bar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
