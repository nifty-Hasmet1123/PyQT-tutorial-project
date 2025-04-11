from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
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

# List of buttons
class Buttons(Enum):
    LIST_OF_BUTTON = list(r"789/456*123-0.=+")



### main object ###
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(250, 300)


### Create Objects and Layouts here ###
master_layout = QVBoxLayout()
master_grid = QGridLayout()

text_box = QLineEdit()
text_box_field = QHBoxLayout()
text_box_field.addWidget(text_box)

clear_and_delete_layout = QHBoxLayout()
clear_button = QPushButton("C")
delete_button = QPushButton("<")
clear_and_delete_layout.addWidget(clear_button)
clear_and_delete_layout.addWidget(delete_button)

# adding a unique identifier
clear_button.setObjectName("clear_button")
delete_button.setObjectName("delete_button")

### Design our app and create ###
def button_clicked(sender):
    text = sender.text()

    if text == "=":
        try:
            # get the current text inside the text_box
            expression = text_box.text()
            
            # use eval() function to evaluate a string expression '3 + 3' output: 4 
            # NOTE: use simpleeval module instead for safety
            res = eval(expression, {"__builtins__": None}, {})
            
        except ZeroDivisionError as e:
            text_box.setText("Zero Division Error")
            raise ValueError(f"Expression: '{expression}' is not valid.") from e
        else:
            text_box.setText(str(res))

    elif text == "C":
        text_box.setText("")
    else:
        text_box.setText(text_box.text() + text)
    
def button_creation(grid):
    row, col = 0, 0
    
    for character in Buttons.LIST_OF_BUTTON.value:
        button = QPushButton(character)
        # identifier = f"calc{character}"
        # button.setObjectName(identifier)
        
        ### attached a function here for every function.
       
        # Capture the current button in during the loop instead of "button.clicked.connect(lambda: button_clicked(button))" which will caused the text_box to only show "+" sign on every button.

        button.clicked.connect(lambda b=button, *args: button_clicked(b))

        # cannot use keyword parameter here because the module is built on C++
        grid.addWidget(button, row, col) 
        
        col += 1

        if col > 3:
            col = 0
            row += 1
    

### returns a map of QPushButton in the grid
# buttons_in_grid = button_creation(master_grid)
button_creation(master_grid)


# adding css on the clear and delete button

clear_button.setStyleSheet("""
    #clear_button {
        padding: 10px;
    }
""")
delete_button.setStyleSheet("""
    #delete_button {
        padding: 10px;
    }
""")

# adding functionalities to the clear and delete button
def delete_button_func():
    current_text = text_box.text()

    if len(current_text) > 1:
        delete_last_text = current_text[:-1]
        text_box.setText(delete_last_text)
    elif len(current_text) <= 1:
        text_box.clear()
        

clear_button.clicked.connect(lambda: text_box.clear())
delete_button.clicked.connect(delete_button_func)

### EVENT ###




### Show/Run our App ###
if __name__ == "__main__":
    # add the grid and text_box_field to the master layout
    # NOTE: The order matters here.
    master_layout.addLayout(text_box_field)
    master_layout.addLayout(master_grid)
    master_layout.addLayout(clear_and_delete_layout)
    
    # finalize the layout using the master layout in the main window
    main_window.setLayout(master_layout)

    main_window.show()
    app.exec_()