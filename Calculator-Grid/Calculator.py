from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QGridLayout,
    QLineEdit
)
from enum import Enum
import sys

# List of buttons
class Buttons(Enum):
    LIST_OF_BUTTON = list(r"789/456*123-0.=+")

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        # layouts
        self.master_layout = QVBoxLayout()
        self.master_grid = QGridLayout()
        self.clear_and_delete_layout = QHBoxLayout()
        self.text_box_field = QHBoxLayout()
        
        # Widgets UI Elements
        self.text_box = QLineEdit()
        self.clear_button = QPushButton("C")
        self.delete_button = QPushButton("<")

        # window configuration
        self.setWindowTitle("Calculator by Maximo Ignacio")
        self.resize(250, 300)

        # add widgets and add object names
        self.add_widgets()
        self.add_object_names()

        # Designs
        self.add_styles()

        # add functionalities
        self.add_functions()

        # adding to layouts to masters
        self.master_layout.addLayout(self.text_box_field)
        self.master_layout.addLayout(self.master_grid)
        self.master_layout.addLayout(self.clear_and_delete_layout)

        # add the final layout
        self.setLayout(self.master_layout)

    def add_widgets(self):
        self.text_box_field.addWidget(self.text_box)
        self.clear_and_delete_layout.addWidget(self.clear_button)
        self.clear_and_delete_layout.addWidget(self.delete_button)
    
    def add_object_names(self):
        self.clear_button.setObjectName("clear_button")
        self.delete_button.setObjectName("delete_button")
    
    def add_styles(self):
        self.clear_button.setStyleSheet("""
            #clear_button {
                padding: 10px;
                max-width: 400px
            }
        """)
        
        self.delete_button.setStyleSheet("""
            #delete_button {
                padding: 10px;
                max-width: 400px
            }
        """)
    
    # overrides the closeEvent method from the QWidget class
    def closeEvent(self, event):
        print("Calculator has been closed.")
        event.accept()
        
    def add_functions(self):
        # for delete button function
        self.delete_button.clicked.connect(self._delete_button_func)
        # for clearing the field
        self.clear_button.clicked.connect(lambda: self.text_box.clear())
        # for adding an event trigger function to the grid buttons
        self._button_creation()

    def _delete_button_func(self):
        current_text = self.text_box.text()

        if len(current_text) > 1:
            sliced_text = current_text[:-1] # exclusive at the end
            self.text_box.setText(sliced_text)
        elif len(current_text) <= 1:
            self.text_box.clear()

    def _button_clicked(self, sender: QPushButton):
        text = sender.text()

        if text == "=":
            try:
                expression = self.text_box.text()
                res = eval(expression, {"__builtins__": None}, {})
            except ZeroDivisionError as e:
                self.text_box.setText("Zero Division Error")
                raise ValueError(f"Expression: '{expression}' is not valid.") from e
            else:
                self.text_box.setText(str(res))
        elif sender.objectName() == "clear_button":
            self.text_box.setText("")
        else:
            self.text_box.setText(self.text_box.text() + text)

    def _button_creation(self):
        row, col = 0, 0

        for character in Buttons.LIST_OF_BUTTON.value:
            button = QPushButton(character)
            button.clicked.connect(lambda b=button, *args: self._button_clicked(b))
            
            # add every widget to the grid layout
            self.master_grid.addWidget(button, row, col)

            col += 1

            if col > 3:
                col = 0
                row += 1

if __name__ == "__main__":
    print("Opening Calculator Application...")
    try:
        app = QApplication(sys.argv)
        main_window = Calculator()
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print("Error:", e)

    