import sys
import os
# from PySide6.QtCore import Qt
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QFileDialog
)
from PySide6.QtGui import QCursor, QPixmap
from enum import Enum
from CustomListWidget import CustomListWidget

class Constants(Enum):
    ITEMS = ["Mouse", "Cat", "Dog"]
    COMBO_BOX = ["Original", "Left", "Right", "Mirror", "Sharpen", "B/W", "Color", "Contrast", "Blur"]

class ImageEditorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor Application")
        self.resize(1080, 720)

        # Layouts
        self.master_layout = QVBoxLayout()
        self.master_row = QHBoxLayout()

        # left side vertical layout
        self.left_layout = QVBoxLayout()

        # right side vertical layout
        self.right_layout = QVBoxLayout()
        
        # Widgets
        self.select_folder_button = QPushButton("Select Folder")
        self.file_list = CustomListWidget() # added modification on pointer
        self.picture_box = QLabel("Image will appear here.")
        self.filter_box = QComboBox()

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.btn_mirror = QPushButton("Mirror")
        self.btn_sharpness = QPushButton("Sharpen")
        self.btn_gray = QPushButton("B/W")
        self.btn_color = QPushButton("Color")
        self.btn_contrast = QPushButton("Contrast")
        self.btn_blur = QPushButton("Blur")

        # sample
        # self.select_folder_button.clicked.connect(fn.get_working_directory)
        self.select_folder_button.clicked.connect(self.get_working_directory)

        # Design and add widget
        self.add_widget_to_list()
        self.add_item_to_combo_box()

        # Design left
        self.left_layout_add_widgets()

        # Design right
        self.right_layout_add_widgets()

        # Adding the final design to the master row layout
        self.add_layout_to_master_row()

        # Set master layout
        self.master_layout.addLayout(self.master_row)
        
        # styling
        self.add_styles()

        # Set final QWidget layout
        self.setLayout(self.master_layout)
    
    # NOTE: better to put this on another file instead 
    # NOTE: CAN ALSO BE USED AS A INSTANCE METHOD BUT IT REALLY SHOULD BE SEPERATE
    # NEXT TASK: AFTER GETTING THE PATH HERE USE OS.LISTDIR() TO LIST ALL FILES AND USE .endswith for every string that ends with .jpg, .png, .jpeg and .bmp
    @staticmethod
    def get_working_directory():
        file_path = QFileDialog.getExistingDirectory()
        return file_path

    def left_layout_add_widgets(self):
        # adding the widgets to the left layout
        buttons = [
            self.btn_left, 
            self.btn_right, 
            self.btn_mirror, 
            self.btn_sharpness, 
            self.btn_gray, 
            self.btn_color, 
            self.btn_contrast, self.btn_blur
        ]

        self.left_layout.addWidget(self.select_folder_button)
        self.left_layout.addWidget(self.file_list)
        self.left_layout.addWidget(self.filter_box)

        for button in buttons:
            self.left_layout.addWidget(button)

    def right_layout_add_widgets(self):
        # adding the widgets to the right layout
        self.right_layout.addWidget(self.picture_box, alignment=Qt.AlignCenter)
    
    def add_layout_to_master_row(self):
        self.master_row.addLayout(self.left_layout)
        self.master_row.addLayout(self.right_layout)

    def add_widget_to_list(self):
        # for item in Constants.ITEMS.value:
        #     self.file_list.addItem(item)
        # add the functionalities here after selecting the select_folder using the QTFileDialog
        # the Editor class here


        pass

    def add_item_to_combo_box(self):
        for item in Constants.COMBO_BOX.value:
            self.filter_box.addItem(item)

    def add_styles(self):
        # Adding a class attribute (html) like style in PyQt
        self.file_list.setProperty("class", "left-widget")
        # print(self.file_list.property("class"))
        self.select_folder_button.setObjectName("select-folder")
        print(self.select_folder_button.objectName())
        
        self.file_list.setStyleSheet("""
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