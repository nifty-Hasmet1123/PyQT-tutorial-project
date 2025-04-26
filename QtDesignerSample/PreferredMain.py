# create a class inhereting from the Ui_Widget class from the compiled version of the widget.ui

from PySide6.QtWidgets import QWidget, QApplication
from widget_ui import Ui_Widget
import sys

class MainWidget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # set up the  design and pass in the current widget class
        self.setWindowTitle("UI Widget Inheritance")
        self.set_design()
    
    def set_design(self):
        # set all qlineedit instance to have this design
        with open("pref_main.css", "r") as file:
            css_style = file.read()
            # print(css_style) # it's okay to add comments on the css design
            self.setStyleSheet(css_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec())