# Import modules
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#   QApplication,
#   QWidget,
#   QVBoxLayout,
#   QHBoxLayout,
#   QLabel,
#   QPushButton
# )

### PROCEDURAL CODE STRUCTURE LEARNING ONLY ### 

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton
)
from functools import partial

### Main app objects ###
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(500, 400)


### Create all App objects ###

title_text = QLabel("Counter")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")
# setting a unique identifier for the button instance/object (to be called in the function for it to be counted.)
button1.setObjectName("button1")
button2.setObjectName("button2")
button3.setObjectName("button3")



### Design our app ###
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# adding the widget on each row
row1.addWidget(title_text, alignment=Qt.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1, alignment=Qt.AlignCenter)
row3.addWidget(button2, alignment=Qt.AlignCenter)
row3.addWidget(button3, alignment=Qt.AlignCenter)


# adding the layout to the master layout per row
for row in [row1, row2, row3]:
    master_layout.addLayout(row)
    
# then finally, adding the final layout to the main_window.
main_window.setLayout(master_layout)



### Events ###
# create a callback function
# def on_button2_clicked():
#     text2.setText("clicked")
# button2.clicked.connect(on_button2_clicked)

# NOTE: when you want arguments in the function you can use lambda or partial function from functools. Here is a example for both.

# adding count of number has been pressed. Make this into a dictionary for 'partial' function to work as expected in re-rendering the count values.
button1_pressed_count = { "value": 0 }
button2_pressed_count = { "value": 0 }
button3_pressed_count = { "value": 0 }

def on_clicked_change_text(label_object, text, sender=None):
    # set the variable count globally python get's confused because it is treating it as local.
    global button1_pressed_count, button2_pressed_count, button3_pressed_count

    if isinstance(label_object, QLabel):
        # the sender or QPushButton object have a method called objectName where it returns the string you dedicated to the button.
        if sender and sender.objectName() == "button1":
            button1_pressed_count["value"] += 1
            
        elif sender and sender.objectName() == "button2":
            button2_pressed_count["value"] += 1
           
        elif sender and sender.objectName() == "button3":
            button3_pressed_count["value"] += 1
            
        label_object.setText(text)
    else:
        raise ValueError("on_clicked_change_text func label_object not an instance of QLabel.")



# using lambda
button1.clicked.connect(
    lambda: on_clicked_change_text(
        text1, 
        text=f"Count button1 clicked {button1_pressed_count['value']} ", 
        sender=button1
    )
)

# using partial (cannot used partial in this case because it is evaluating the original value. To solve this create a dictionary instead)
# button2.clicked.connect(
#     partial(
#         on_clicked_change_text, 
#         label_object=text2, 
#         text=f"Count button clicked: {button2_pressed_count['value']} ",
#         sender=button2
#     )
# )
button2.clicked.connect(
    lambda: on_clicked_change_text(
        text2, 
        text=f"Count button2 clicked: {button2_pressed_count['value']}",
        sender=button2
    )
)

# won't work because of the setup of the function
# button3.clicked.connect(
#     partial(
#         on_clicked_change_text,
#         label_object=text3,
#         text=f"Count button clicked: {button3_pressed_count['value']}",
#         sender=button3
#     )
# )
button3.clicked.connect(
    lambda: on_clicked_change_text(
        label_object=text3,
        text=f"Count button3 clicked: {button3_pressed_count['value']}",
        sender=button3
    )
)

### Show/Run our App ###
if __name__ == "__main__":
    main_window.show()
    app.exec_()
