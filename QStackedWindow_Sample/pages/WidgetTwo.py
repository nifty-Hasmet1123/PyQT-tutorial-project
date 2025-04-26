from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout, 
    QLabel
)

class WidgetTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(QLabel("Widget Two"))
        self.setLayout(self.main_layout)
