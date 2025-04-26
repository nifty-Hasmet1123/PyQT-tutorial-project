from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QSizePolicy
from PySide6.QtCore import QObject, Qt
import sys

loader = QUiLoader()
widget_ui_path = "widget.ui" # widget.ui is at root folder (on this directory)

class UserInterface(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load(widget_ui_path)
        self.ui.setWindowTitle("User Data")
        self.ui.resize(1080, 720)
        self.ui.submit_button.clicked.connect(self.click_button_signal)

        # custom modification on the widget.ui file    
        self.set_custom_design()
    
    def set_custom_design(self):
        fullname_label = self.ui.label
        occupation_label = self.ui.label_2
        
        fullname_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        occupation_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # ---------------------------
        full_name_line_edit = self.ui.full_name_line_edit
        occupation_line_edit = self.ui.occupation_line_edit

        full_name_line_edit.setStyleSheet("""
            QLineEdit {
                margin-left: 10px;
            }
        """)

        # full_name_line_edit
        full_name_line_edit.setFixedSize(210, 20)
        occupation_line_edit.setFixedSize(200, 20)

        # --------------------------
        self.ui.submit_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # --------------------------
        master_layout = self.ui.verticalLayout
        master_layout.setAlignment(Qt.AlignTop)

        self.ui.horizontalLayout_2.setAlignment(Qt.AlignLeft)
        self.ui.horizontalLayout.setAlignment(Qt.AlignLeft)
        

    def click_button_signal(self):
        # print(f"{self.ui.full_name_line_edit.text()}")
        line_edit_full_name_object_name = self.ui.full_name_line_edit.objectName()
        line_edit_occupation_object_name = self.ui.occupation_line_edit.objectName()
        print(f"Line Edit Object Name: '{line_edit_full_name_object_name}' and '{line_edit_occupation_object_name}'")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface()
    window.ui.show()
    sys.exit(app.exec())