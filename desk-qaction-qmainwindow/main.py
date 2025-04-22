
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction
import sys

class Main(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application
        self.setWindowTitle("Desktop Application")
        self.resize(1080, 720)
        self.menuBar().setNativeMenuBar(False)
        # buttons menu bar
        self.create_menu_bar()
        self.create_status_bar()
        self.create_toolbar()
        self.set_central_widgets()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        # file menu
        file_menu = menu_bar.addMenu("&File") # & make the File a shortcut like alt + F
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.close)
        # font = file_menu.font()
        # font.setBold(True)
        # file_menu.setFont(font)

        # edit menu
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

    def create_toolbar(self):
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # add action to the toolbar
        quit_action_toolbar = QAction("Quit", self)
        quit_action_toolbar.setStatusTip("Quit the program.")
        quit_action_toolbar.triggered.connect(self.close)

        # NOTE: if you have a self.quit_action on the instance attribute you can just passed that in here since it is inherting from the QAction class
        toolbar.addAction(quit_action_toolbar)

        # some action
        action = QAction("Some action", self)
        action.setStatusTip("Status message for some actions.")
        action.triggered.connect(self.print_on_action)
        toolbar.addAction(action)

        # action with a png file
        # action = QAction(QIcon("start.png"), "Some other action", self)

        # adds a separator to the toolbar
        toolbar.addSeparator()
        
        # add a button in the toolbar
        click_button = QPushButton("click me")
        click_button.clicked.connect(self.click_here_fn)
        toolbar.addWidget(click_button)

        # another way
        click_button_2 = QAction("click me", self)
        click_button_2.setStatusTip("hovered over the click_button_2")
        click_button_2.triggered.connect(lambda: self.statusBar.showMessage("button was clicked!!!"))
        toolbar.addAction(click_button_2)

    def set_central_widgets(self):
        my_label = QLabel("THIS IS THE CENTRAL WIDGET", alignment=Qt.AlignCenter)
        self.setCentralWidget(my_label)

    def create_status_bar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setStyleSheet("""
            QStatusBar {
                border: 1px solid grey;
                color: white;
                font-size: 16px;
                font-style: italic;
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 0, 
                    stop: 0 #1e3c72,
                    stop: 1 #2a5298                 
                );
            }
        """)

    def print_on_action(self):
        print("Action was hovered.")

    def click_here_fn(self):
        # self.statusBar.showMessage("Click here was clicked!!!")
        self.statusBar.showMessage("Click here was clicked!!!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main(app)
    window.show()
    sys.exit(app.exec())
