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
    QFileDialog,
    QMessageBox
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
        self.selected_file = None
        self.file_path_selected = None

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
        self.info_box = QLabel("")
        self.filter_box = QComboBox()

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.btn_mirror = QPushButton("Mirror")
        self.btn_sharpness = QPushButton("Sharpen")
        self.btn_gray = QPushButton("B/W")
        self.btn_color = QPushButton("Color")
        self.btn_contrast = QPushButton("Contrast")
        self.btn_blur = QPushButton("Blur")

        # PixMap
        self.pixmap = QPixmap()

        # sample
        # self.select_folder_button.clicked.connect(fn.get_working_directory)
        # passing the main class(self) to the static method function
        self.select_folder_button.clicked.connect(lambda: self.get_working_directory(self))
       
        # Design and add widget
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

        # set the signal on the emit mousePressEvent
        # doesn't need to supply with argument
        # add a connect on the fileSelected class attribute in the CustomListWidget
        self.file_list.fileSelected.connect(self.on_file_select)

    ### Call this method on_file_select method
    def display_image_based_on_path(self):
        # also add this in the 
        if self.file_path_selected and os.path.exists(self.file_path_selected):
            # self.file_path_selected = B:/CODES/Python-Related/PYQT-PROJECT/Image-Editing-App/assets

            ### DEBUGGING PURPOSES
            # QMessageBox.information(self, "Debug info", f"Path: {self.file_path_selected}")
            # QMessageBox.information(self, "Debug info", f"Path: {self.selected_file}")
            image_path = os.path.join(self.file_path_selected, self.selected_file)
            
            # Load the image into the existing pixmap instance
            self.pixmap.load(image_path)

            # add scaling to the picture box
            self.picture_box.setPixmap(self.pixmap)

             
    def on_file_select(self, file_name):
        # the file name will come from the CustomListWidget mousePressEvent instance method
        # print(f"Selected picture was: {file_name}")
        self.selected_file = file_name
        # self.picture_box.setText(f"You have selected this file: {self.selected_file}") # now display the image here instead of QLabel

        ### add the widget to the right column if the selected_file change
        if self.selected_file:
            # NOTE: you can add a html label on the setText method of QLabel
            
            # display the image here after selecting
            self.display_image_based_on_path()

            # HTML STRING
            html_string = "You have selected file: <strong>{text}</strong>".format(text=self.selected_file)

            self.info_box.setText(html_string)
            self.right_layout.insertWidget(0, self.info_box, alignment=Qt.AlignLeft)
    
    # NOTE: better to put this on another file instead 
    # NOTE: CAN ALSO BE USED AS A INSTANCE METHOD BUT IT REALLY SHOULD BE SEPERATE
    # NEXT TASK: AFTER GETTING THE PATH HERE USE OS.LISTDIR() TO LIST ALL FILES AND USE .endswith for every string that ends with .jpg, .png, .jpeg and .bmp
    @staticmethod
    def get_working_directory(cls_instance):
        """
        This is a function that should be outside the class because it provides a function not really related to this class but can be used by it.
        
        Args:
            cls_instance = should be an argument of class itself(self) in order for this to work. Do not pass the literal class name because it will not work
            This will only work if the .add_widget_to_list() has a decorator of @classmethod
        
        """
        file_path = QFileDialog.getExistingDirectory()

        ### add the functionalities here to be displayed in the file list for display
        
        # add the file path to tthe current instance of the class
        cls_instance.file_path_selected = file_path

        # call the function add_widget_to_list to display the files that are selected on the directory only .png, .jpeg, .jpg will be shown
        cls_instance.add_widget_to_list(file_path)
        
        # return file_path

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

    def add_widget_to_list(self, path: str):
        list_of_file = os.listdir(path)
        
        for file in list_of_file:
            if file.endswith(("png", "jpeg", "bmp", "jpg")):
                self.file_list.addItem(file)
            
    def add_item_to_combo_box(self):
        for item in Constants.COMBO_BOX.value:
            self.filter_box.addItem(item)

    def add_styles(self):
        # Adding a class attribute (html) like style in PyQt
        self.file_list.setProperty("class", "left-widget")
        # print(self.file_list.property("class"))
        self.select_folder_button.setObjectName("select-folder")
        # print(self.select_folder_button.objectName())
        
        # info box
        self.info_box.setFixedHeight(20)

        # picture box
        

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