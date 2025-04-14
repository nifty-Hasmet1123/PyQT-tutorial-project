### create a save button to save the image

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    # QListWidget,
    # QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from classes.ImageEditorDesigns import ImageEditorDesigns, CustomListWidget
from classes.ImageEditorFunctions import ImageEditorFunctions

class ImageEditorWidgets(QWidget):
    def __init__(self):
        super().__init__()
        # initials
        self.setWindowTitle("Image Editor")
        self.resize(1080, 720)
        self.file_path: str = None
        self.image_exact_path = None

        # use the ImageEditorDesign for design of certain widgets
        self.ied_designs = ImageEditorDesigns(self)

        # use the ImageEditorFunctions for button functionalities
        self.ief_fn = ImageEditorFunctions(self)

        # master layouts
        self.master_layout = QVBoxLayout()
        self.master_row = QHBoxLayout()

        # left layout
        self.left_layout = QVBoxLayout()

        # right layout
        self.right_layout = QVBoxLayout()

        # left layout widgets
        self.select_folder_button = QPushButton("Select Folder")
        self.file_list = CustomListWidget()
        self.combo_box = QComboBox()

        # right layout widgets
        self.pixmap = QPixmap()
        self.picture_box = QLabel("Please select a picture.")

        # attached the fileSelected emiter here # HAS BEEN CHANGE SEE ImageEditorDesigns at line 37
        # self.file_list.fileSelected.connect(self.ief_fn.on_file_select_emit)
        self.file_list.SIGNAL.fileSelected.connect(self.ief_fn.on_file_select_emit)
        
        # add a text change event to the combo box to get current text of the box
        self.combo_box.currentTextChanged.connect(self.ief_fn.combo_box_function)
        
    def image_editor_widgets(self):
        # call the function for design and functionalities
        self.set_design_and_functionalities()

        self.left_layout.addWidget(self.select_folder_button)
        self.left_layout.addWidget(self.file_list)
        self.left_layout.addWidget(self.combo_box)
        self.right_layout.addWidget(self.picture_box, alignment=Qt.AlignCenter)

    def set_design_and_functionalities(self):
        # object names here
        self.set_object_naming()
        # add the designs here after creating the widgets
        self.set_designs()
        # set the combox box values in here
        self.set_combo_box_values()
        # add function to the select folder
        self.select_folder_button.clicked.connect(self.ief_fn.select_folder_function)

    def set_combo_box_values(self):
        combo_box = ["Original", "Left", "Right", "Mirror", "Sharpen", "B/W", "Color", "Contrast", "Blur"]

        for item in combo_box:
            self.combo_box.addItem(item)

    def set_object_naming(self):
        self.file_list.setObjectName("widget_file_list")
        self.select_folder_button.setObjectName("widget_btn_select_folder")

    def set_designs(self):
        self.ied_designs.add_q_list_style()
        self.ied_designs.add_select_folder_btn_style()

    def setup_layout(self):
        ### all the initial setup of layout will be done here
        self.image_editor_widgets()
        
        self.master_row.addLayout(self.left_layout)
        self.master_row.addLayout(self.right_layout)

        self.master_layout.addLayout(self.master_row)
        
        # take the full display in the main window
        # self.master_layout.setContentsMargins(0, 0, 0, 0)
        # self.master_layout.setSpacing(0)
        # self.master_row.setContentsMargins(0, 0, 0, 0)
        # self.master_row.setSpacing(0)

        self.setLayout(self.master_layout)
    