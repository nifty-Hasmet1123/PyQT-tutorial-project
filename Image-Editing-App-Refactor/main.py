### Main Window of the Application
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QListView,
    QLabel,
    QVBoxLayout,
    QApplication,
    QWidget
)
from classes.ImageEditorWidgets import ImageEditorWidgets


# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Image Editor")
#         self.resize(1080, 720)
    
#         self.label_sample = QLabel("Hello")
#         self.master_layout = QVBoxLayout()
#         self.master_layout.addWidget(self.label_sample)    
        
#         # Create a QWidget container
#         container = ImageEditorWidgets()
#         container.image_editor_widget_set_layout()

#         # Set it as the central widget
#         # self.setCentralWidget(container)
#         self.setLayout(container)

class Main():
    def __init__(self):
        self.container = ImageEditorWidgets()
        self.container.setup_layout()

    def show(self):
        self.container.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())

        