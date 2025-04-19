from PySide6.QtCore import QThread, Signal
import requests

class APIWorker(QThread):
    result_signal = Signal(str)

    def __init__(self, api_type):
        super().__init__()
        self.api_type = api_type

    # this is an instance method within the QThread application we are overwriting this function.
    def run(self):
        try:
            if self.api_type == "first":
                response = requests.get("http://127.0.0.1:5000", timeout=90)

                if response.ok:
                    data = response.json()
                    message = data.get("message", "No message received.")
                    self.result_signal.emit(message)
            elif self.api_type == "second":
                response = requests.get("http://127.0.0.1:5000/api", timeout=90)

                if response.ok:
                    data = response.json()
                    message = data.get("message", "No message received.")
                    self.result_signal.emit(message)
        
        except Exception as e:
            print(f"ERROR WAS MADE: {e}")
            self.result_signal.emit(f"Error: {e}")
        
