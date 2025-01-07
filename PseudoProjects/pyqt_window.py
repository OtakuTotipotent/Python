from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 300, 200)
        label = QLabel("Hello, PyQt!", self)
        label.move(100, 80)

app = QApplication([])
# app.setStyleSheet("QLabel { color: blue; font-size: 16px; }")
window = MainWindow()
window.show()
app.exec()
