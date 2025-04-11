import sys
# from PySide6.QtCore import Qt
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QComboBox
)
from PySide6.QtGui import QCursor
from enum import Enum
from CustomListWidget import CustomListWidget

class Constants(Enum):
    ITEMS = ["Mouse", "Cat", "Dog"]

class ImageEditorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor Application")
        self.resize(750, 500)

        # Layouts
        self.master_layout = QVBoxLayout()
        self.master_row = QHBoxLayout()

        # left side vertical layout
        self.left_layout = QVBoxLayout()

        # right side vertical layout
        self.right_layout = QVBoxLayout()
        
        # continue by tomorrow

        # Widgets
        self.select_folder_button = QPushButton("Select Folder")
        self.list_widget = CustomListWidget()
        self.sample_button = QPushButton("Sample button")

        # Design and add widget
        self.add_widget()

        # Design





        

        # Set master layout
        self.master_layout.addLayout(self.master_row)
        
        # styling
        self.add_styles()

        # Set final QWidget layout
        self.setLayout(self.master_layout)

    def left_layout_design(self):
        pass

    def add_widget(self):
        for item in Constants.ITEMS.value:
            self.list_widget.addItem(item)

    def add_styles(self):
        # Adding a class attribute (html) like style in PyQt
        self.list_widget.setProperty("class", "left-widget")
        # print(self.list_widget.property("class"))
        self.select_folder_button.setObjectName("select-folder")
        print(self.select_folder_button.objectName())
        
        self.list_widget.setStyleSheet("""
            QListWidget[class='left-widget'] {
                max-width: 200px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                color: red;
            }
        """)

        self.select_folder_button.setStyleSheet("""
            QPushButton#select-folder {
                max-width: 300px;
                width: 200px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        # NOTE: Some of the CSS pseudo-selector and pseudo-class selectors are not supported directly by writing CSS code you need to use the python QtGUI for this.
        self.select_folder_button.setCursor(QCursor(Qt.PointingHandCursor))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ImageEditorApp()
    main_window.show()
    sys.exit(app.exec())