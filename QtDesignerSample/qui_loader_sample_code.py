from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
import sys

### NOTE: DON'T USE QUiLoader in production as it hinders the user experience in using the application


# set up a loader object
loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None) # Load the ui - happens at run time!

def do_something():
    # access the object names based on the qt designer
    print(f"Line edit 1: {window.full_name_line_edit.text()} || Line edit 2: {window.occupation_line_edit.text()}")

window.submit_button.clicked.connect(do_something)
window.setWindowTitle("User data")
window.show()
sys.exit(app.exec())