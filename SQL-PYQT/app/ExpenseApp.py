from PySide6.QtWidgets import (
    QLabel,
    QPushButton, 
    QLineEdit,
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QVBoxLayout, 
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

# query the details here as well NOTE: should be seperated
from config.db import engine
from config.models import ExpenseModel
from sqlalchemy.orm import sessionmaker

class ExpenseApp(QWidget):
    # created a SESSION HERE
    Session = sessionmaker(bind=engine)

    def __init__(self):
        super().__init__()
        self.resize(1080, 720)
        self.setWindowTitle("Expense Tracker 2.0")

        # layout
        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        

        # widgets
        self.date_box = QDateEdit()
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()
        self.add_button = QPushButton("Add Expense")
        self.delete_button = QPushButton("Delete Expense")

        self.table = QTableWidget()
        self.table.setColumnCount(5) # id, date, category, amount, description
        self.table.setHorizontalHeaderLabels([
            "Id", "date", "category", "amount", "description"
        ])

        # Designs
        self.row1_widget()
        self.row2_widget()
        self.row3_widget()

    
        # add to master layout
        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)
         # add table
        self.master_layout.addWidget(self.table)

        # load the table with values from the database
        self.load_table()

        # EVENTS
        self.add_button.clicked.connect(self.add_expense)

        # final layout
        self.setLayout(self.master_layout)

    def row1_widget(self):
        self.row1.addWidget(QLabel("Date:"))
        self.row1.addWidget(self.date_box)
        self.row1.addWidget(QLabel("Category:"))

        self.dropdown.addItems([
            "Food",
            "Transportation",
            "Rent",
            "Shopping",
            "Entertainment",
            "Bills",
            "Others"
        ])

        self.row1.addWidget(self.dropdown)

    def row2_widget(self):
        self.row2.addWidget(QLabel("Amount:"))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description"))
        self.row2.addWidget(self.description)

    def row3_widget(self):
        self.row3.addWidget(self.add_button)
        self.row3.addWidget(self.delete_button)

    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText() or "No value provided."
        amount = self.amount.text() or "No value provided."
        description = self.description.text() or "No value provided."

        confirm_box = QMessageBox.question(
            self,
            "Confirm Add",
            f"Are you sure you want to add this expense?\n\nDate: {date}\nCategory: {category}\nAmount: {amount}\nDescription: {description}",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm_box == "Yes":
            print(True)
        else:
            print(False)

    def load_table(self):
        self.table.setRowCount(0)
        session = self.Session()
        
        # select * from "expenses"
        data = session.query(ExpenseModel).all()
        # column_list = len(ExpenseModel.__table__.columns)
        expense_model_column = ExpenseModel.__table__.columns  
        
        
        for row_idx, expense in enumerate(data):
            # expense will return an object <config.models.ExpenseModel object at 0x00000170EB4A9E50>

            # set the value in the row
            self.table.insertRow(row_idx)
            
            # simple usage of the .setItem on table
            # self.table.setItem(row_idx, 0, QTableWidgetItem(str(expense.id)))
            # self.table.setItem(row_idx, 1, QTableWidgetItem(str(expense.category)))
            # self.table.setItem(row_idx, 2, QTableWidgetItem(str(expense.amount)))
            # self.table.setItem(row_idx, 3, QTableWidgetItem(str(expense.description)))

            # loop thru the column then add the data you get from the row
            for col_idx, column_properties in enumerate(expense_model_column):
                # column_properties = expenses.category, expenses.amount, expenses.description

                # get the data from the object model for each column
                # for every expense object access there name.
                value = getattr(expense, column_properties.name)

                self.table.setItem(
                    row_idx,
                    col_idx,
                    QTableWidgetItem(str(value))
                )

                # getattr example
                # class Person:
                #     def __init__(self, name, age):
                #         self.name = name
                #         self.age = age

                # # Create an instance of Person
                # person = Person("Alice", 30)

                # # Access the attributes using getattr()
                # name = getattr(person, 'name')  # Access the 'name' attribute
                # age = getattr(person, 'age')  # Access the 'age' attribute

                # print(f"Name: {name}, Age: {age}")

