from PySide6.QtWidgets import QWidget, QApplication
from stacked import Ui_Form
import sys


### I have tried creating a stacked widget in the QT Designer multiple widget using different stacked
class Test(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(1) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())