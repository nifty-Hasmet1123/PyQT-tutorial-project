from PySide6.QtWidgets import (
    QVBoxLayout,
    QListWidget,
    QWidget,
    QLabel,
    QHBoxLayout, 
    QListWidgetItem,
    QStackedWidget
)

from pages.WidgetOne import WidgetOne
from pages.WidgetTwo import WidgetTwo
from pages.WidgetThree import WidgetThree
from PySide6.QtCore import Qt

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        ########################################
        # layouts
        self.main_layout = QVBoxLayout()
        self.main_row = QHBoxLayout()
        self.left_box = QVBoxLayout()
        # self.right_box = QVBoxLayout()
        self.right_stack = QStackedWidget()
        ########################################
        # widgets and design
        self.list_widget = QListWidget()
        self.list_widget.setFixedWidth(250)
        
        ########################################
        # helper methods
        self.set_widget_left_box()

        self.list_widget.setCurrentRow(0) # initially select the row first here 
        self.page_trigger()
        ########################################
        # functions
        self.list_widget.clicked.connect(self.page_trigger)
        ########################################
        # add layouts
        self.main_row.addLayout(self.left_box)
        # self.main_row.addLayout(self.right_box)
        self.main_row.addWidget(self.right_stack)
        self.main_layout.addLayout(self.main_row)
        self.setLayout(self.main_layout)
        
    def set_widget_left_box(self):
        for i in range(1, 4):
            self.list_widget.addItem(
                QListWidgetItem(f"Page {i}")
            )
           
        self.left_box.addWidget(self.list_widget)
        
    def set_widget_right_box(self, qwidget):
        self.right_stack.addWidget(qwidget)

    # on clicked for each Page trigger
    def page_trigger(self):
        # self.clear_layout(self.right_box)
        current_row = self.list_widget.currentRow()
        
        widget = None
        if current_row == 0:
            widget = WidgetOne()
        elif current_row == 1:
            widget = WidgetTwo()
        elif current_row == 2:
            widget = WidgetThree()
        
        if widget:
            self.set_widget_right_box(widget)
            self.right_stack.setCurrentIndex(current_row)

    def clear_layout(self, layout):
        while layout.count():
            object_for_deletion = layout.takeAt(0) # returns None if there is no object was found
            widget = object_for_deletion.widget()

            if widget is not None:
                widget.deleteLater()
        
        # REFERENCE: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLayout.html#PySide2.QtWidgets.PySide2.QtWidgets.QLayout.takeAt
    