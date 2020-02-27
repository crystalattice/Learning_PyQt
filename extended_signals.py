from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My awesome app")
        layout = QVBoxLayout()
        for n in range(10):
            btn = QPushButton(str(n))  # For each number in range(), create a button w/ label "n"
            btn.pressed.connect(lambda n=n: self.my_custom_fn(n))  # Pass the button number to the function
            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def my_custom_fn(self, n):
        print(f"Button {n} was clicked")


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
