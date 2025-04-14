from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import QListWidget

class ImageEditorDesigns():
    def __init__(self, instance):
        self.instance = instance
    
    def add_q_list_style(self):
        design = """
            QListView#widget_file_list {
                max-width: 200px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                color: red;
            }
        """
        self.instance.file_list.setStyleSheet(design)
        # QMessageBox.information(self.instance, "Debug info", f"{self.instance.file_list.objectName()}")
    
    def add_select_folder_btn_style(self):
        design = """
            QPushButton#widget_btn_select_folder {
                max-width: 300px;
                width: 200px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """
        self.instance.select_folder_button.setStyleSheet(design)
        self.instance.select_folder_button.setCursor(
            QCursor(Qt.PointingHandCursor)
        )

# You need to inherit from QObject when defining a class with PySide6/PyQt signals because signals and slots only work on classes derived from QObject
class SignalController(QObject):
    fileSelected = Signal(str)

class CustomListWidget(QListWidget):
    # defined a class attribute here to emit the data of which item/picture file that was selected.
    # NOTE: ITS BETTER TO HAVE THIS OUTSIDE OF THIS CLASS TO BE ABLE TO USE IN OTHER PLACES EXAMPLE AT LINE 37
    # fileSelected = Signal(str)

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.SIGNAL = SignalController() # if you create a class with signal on it you can define here as a instance attribute
    
    def mouseMoveEvent(self, event):
        item = self.itemAt(event.pos())

        if item:
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))

        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        item = self.itemAt(event.pos())

        if item:
            # self.fileSelected.emit(item.text()) # connected to line 40
            self.SIGNAL.fileSelected.emit(item.text())
            
        super().mousePressEvent(event)

