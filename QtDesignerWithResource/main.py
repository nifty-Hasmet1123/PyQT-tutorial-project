from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from design_ui import Ui_Widget
import sys

# import the resource
import resource_rc

# import the qwidget from the qt designer
class MyWidget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spin_box.lineEdit().setReadOnly(True)

        self.set_func()

    def set_func(self):
        # import starts with ':' because it has no prefix indicated in the resource when created
        self.add_btn.setIcon(QIcon(":/assets/plus.png"))
        self.minus_btn.setIcon(QIcon(":/assets/minus.png"))

        self.add_btn.clicked.connect(lambda: self.button_func("add"))
        self.minus_btn.clicked.connect(lambda: self.button_func("minus"))

    def button_func(self, method):
        try:
            current_number = int(self.spin_box.text()) 
            
            if method == "add":
                current_number += 1
            elif method == "minus":
                current_number -= 1
            else:
                raise ValueError("Check function arguments!!!")
        except ValueError as err:
            message = { "Error": str(err) }
            QMessageBox.critical(self, "Program Error For Developer", "Check the code for errors or wrong arguments!!!")
            print(message)
        else:
            self.spin_box.setValue(current_number)
        


# create qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MyWidget()
        self.setWindowTitle("Widget Application")
        self.resize(800, 600)
        self.setCentralWidget(self.main_widget)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())