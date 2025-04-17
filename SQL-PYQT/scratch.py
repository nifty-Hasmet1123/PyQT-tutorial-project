import sys
import os
import psycopg2
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget, QMessageBox

def get_connection():
    return psycopg2.connect(
        dbname="pyqt-server",
        user="postgres",
        password="root",
        host="localhost"
    )

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        # connect to a database (you don't need a context manager when using QtSQL)

        # self.db = QSqlDatabase.addDatabase("QODBC")
        # temporary database using QODBC FROM DEVART
        # self.db.setDatabaseName("Driver={Devart ODBC Driver for PostgreSQL};Server=localhost;Port=5432;Database=pyqt-server;Uid=postgres;Pwd=root;")

        # using psycopg2 instead of qsqldatabase
        try :
            with get_connection() as conn:
                QMessageBox.information(self, "Connection Successful", "Successfully connected to the database!")
                print("Database connection successful.")
        except Exception as e:
            print("error: {e}".format(e=e))
        

    def create_table_if_not_exists(self):
        query = self.query

        query.exec_("""
            CREATE TABLE IF NOT EXISTS expenses(
                id SERIAL PRIMARY KEY,
                data TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
        """)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()
    sys.exit(app.exec())    
   