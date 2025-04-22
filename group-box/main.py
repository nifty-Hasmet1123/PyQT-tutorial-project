from PySide6.QtWidgets import QApplication, QMainWindow
from Widget import Widget
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.group_box_widget = Widget()
        self.setWindowTitle("Group Box")
        self.resize(1080, 720)

        self.setCentralWidget(self.group_box_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())