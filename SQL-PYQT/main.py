### using sqlalchemy orm for connectin to the database.

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from config.db import engine, is_connected
from config.models import Base
import sys
from app.ExpenseApp import ExpenseApp

class Main():
    def __init__(self):
        if is_connected == True:
            self.expense_app = ExpenseApp()
            Base.metadata.create_all(engine) # create the table
            
            print("Connection has been established.")
        else:
            QMessageBox.critical(self, "Error", is_connected)
            sys.exit(1)

    def show(self):
        self.expense_app.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
