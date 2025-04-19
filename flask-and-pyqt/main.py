from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)
from PySide6.QtCore import Slot
from QT.api_worker import APIWorker
import sys

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flask API Caller")
        self.resize(1080, 720)

        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()

        self.button = QPushButton("Load API CALLER http://127.0.0.1:5000")
        self.button_api = QPushButton("Load API caller http://127.0.0.1:5000/api")
        self.label = QLabel("Click the button to load data.")
        self.label_api = QLabel("Click the button to load data.")
        self.label.setWordWrap(True)

        # self.master_layout.addWidget(self.button)
        # self.master_layout.addWidget(self.button_api)
        # self.master_layout.addWidget(self.label)

        self.row1.addWidget(self.button)
        self.row1.addWidget(self.label)

        self.row2.addWidget(self.button_api)
        self.row2.addWidget(self.label_api)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        

        # functions 
        self.set_button_style()

        # events
        self.button.clicked.connect(lambda: self.load_data("first", self.label))
        self.button_api.clicked.connect(lambda: self.load_data("second", self.label_api))

        self.setLayout(self.master_layout)

    def set_button_style(self):
        self.button.setMaximumWidth(300)
        self.button_api.setMaximumWidth(300)

    def load_data(self, api_type, label_element):
        self.worker = APIWorker(api_type)
        # the result comes from the emitted string value in the ApiWorker 
        self.worker.result_signal.connect(lambda result: self.show_result(result, label_element))
        self.worker.start()

    @Slot(str)
    def show_result(self, result, label_element):
        label_element.setText(result)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())