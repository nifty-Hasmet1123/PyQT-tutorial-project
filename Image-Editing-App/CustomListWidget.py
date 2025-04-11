from PySide6.QtWidgets import (
    QListWidget
)
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

# creating a custom class inheriting from the QListWidget that adds functionality on having a pointer on the current items only and not on the blank spaces in the list widget
class CustomListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        # enable mouse tracking for hover
        self.setMouseTracking(True)
    
    # a instance method from the QListWidget
    def mouseMoveEvent(self, event):
        # Check if the mouse is over an item
        item = self.itemAt(event.pos())

        if item:
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))

        # Call the parent's (QListWidget's) mouseMoveEvent to keep any default behavior
        # Without super().mouseMoveEvent(event): You will be overriding the entire mouse move event handling. This means that if the parent class (like QListWidget) has any default behavior for mouse movements (like updating the widget, handling hover effects, etc.), it won't happen. Only your custom logic will be executed.
        super().mouseMoveEvent(event)