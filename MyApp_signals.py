import sys  # For command line arguments

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    """Subclass QMainWindow to customize application's main window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set SIGNALS
        self.windowTitleChanged.connect(self.onWindowTitleChange)  # Called whenever the window title changes; passes
        # the new title to the function
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())  # New title is discarded and function called
        # w/o parameters
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))  # Pass new title to function in place of
        # default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))  # Pass new title plus extra parameter

        self.setWindowTitle("My dope app")
        label = QLabel("This is awesome!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)  # Set central widget; allows expansion to fill entire window by default.

    # Set SLOTS
    def onWindowTitleChange(self, s):
        """Accept a string and print it"""
        print(s)

    def my_custom_fn(self, a="HELLO!", b=5):
        """Set default parameters and can be called w/o a value"""
        print(a, b)


app = QApplication(sys.argv)  # Runs event loop; set to capture CLI arguments. To ignore CLI args, use QApplication([]).

window = MainWindow()
window.show()  # Required to display windows; invisible by default.

app.exec_()  # Start event loop; note trailing underscore.
