import sys
from PySide6.QtWidgets import (
    QApplication,
)

from app.InterestCalculator import InterestCalculator

class Main():
    def __init__(self):
        self.application = InterestCalculator()
        self.application.setWindowTitle("Interest Calculator With MatPlotLib")
        self.application.resize(1080, 720)
    
    def show(self):
        self.application.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())