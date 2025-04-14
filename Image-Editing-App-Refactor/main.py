### Main Window of the Application
import sys
from PySide6.QtWidgets import QApplication
from classes.ImageEditorWidgets import ImageEditorWidgets

class Main():
    def __init__(self):
        self.container = ImageEditorWidgets()
        self.container.setup_layout()

    def show(self):
        self.container.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
        