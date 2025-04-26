from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QStackedWidget,
    QMainWindow
)
import sys
from main_widget import MainWidget

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Page")
        self.resize(800, 600)
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
