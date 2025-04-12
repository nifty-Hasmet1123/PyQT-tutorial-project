from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
import sys

class FolderSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select Folder Example")
        self.setGeometry(100, 100, 400, 150)

        self.layout = QVBoxLayout()

        self.select_folder = QPushButton("Select Folder")
        self.select_folder.clicked.connect(self.open_folder_dialog)

        self.label = QLabel("Selected folder path will appear here.")

        self.layout.addWidget(self.select_folder)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def open_folder_dialog(self):
        # folder_path = QFileDialog.getExistingDirectory(self, "Select Folder Dialogue")
        folder_path = QFileDialog.getExistingDirectory()
        # folder_path = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)") # 4th argument to show images
        if folder_path:
            self.label.setText(f"Selected Folder:\n{folder_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderSelector()
    window.show()
    sys.exit(app.exec_())
