from PySide6.QtWidgets import QTabWidget, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from HoverPushButton import HoverPushButton

class CustomTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

    def add_tab(self, widget_instance, label):
        self.addTab(widget_instance, label)
    
class InformationWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window # the qmainwindow in the main.py to access status bar
        self.form_layout = QVBoxLayout()
        self.form_layout.addWidget(QLabel("Full Name: "))
        self.form_layout.addWidget(QLineEdit())
        
        self.form_layout.setAlignment(Qt.AlignTop)
        self.set_design()
        self.setLayout(self.form_layout)

    def set_design(self):
        self.setStyleSheet("""
            QLineEdit {
                max-width: 200px;
            }
        """)

class ButtonWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.master_layout = QVBoxLayout()

        for button in ["One", "Two", "Three"]:
            instance = HoverPushButton(button, main_window)
            instance.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.master_layout.addWidget(instance)

        self.master_layout.setAlignment(Qt.AlignTop)
        
        self.setLayout(self.master_layout)
    
class MainWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.custom_tab_widget = CustomTabWidget()
        self.information_widget = InformationWidget(self.main_window)
        self.button_widget = ButtonWidget(self.main_window)
        self.master_layout = QVBoxLayout()

        # add the tab in the main widget
        self.master_layout.addWidget(self.custom_tab_widget)

        # information tab
        self.custom_tab_widget.add_tab(
            self.information_widget, 
            "Information"
        )
        self.custom_tab_widget.add_tab(
            self.button_widget,
            "Button"
        )

        self.setLayout(self.master_layout)
