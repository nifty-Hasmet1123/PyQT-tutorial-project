from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout, 
    QLabel
)
from PySide6.QtCore import Qt

class WidgetOne(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(QLabel("Widget One"), alignment=Qt.AlignCenter)
        self.set_design()
        self.setLayout(self.main_layout)

    def set_design(self):
        # self.setStyleSheet("""
        #     QWidget {
        #         border: 8px solid grey;
        #     }
        # """)
        pass