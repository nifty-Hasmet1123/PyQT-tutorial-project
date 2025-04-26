from PySide6.QtWidgets import QPushButton

class HoverPushButton(QPushButton):
    def __init__(self, text, main_window):
        super().__init__(text)
        self.main_window = main_window
    
    def enterEvent(self, event):
        current_text = self.text()
        self.main_window.statusBar.showMessage(f"Selected Button: {current_text}")
        super().enterEvent(event)