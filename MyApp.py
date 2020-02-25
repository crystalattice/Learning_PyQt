import sys  # For command line arguments

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)  # Runs event loop; set to capture CLI arguments. To ignore CLI args, use QApplication([]).

window = QMainWindow()
window.show()  # Required to display windows; invisible by default.

app.exec_()  # Start event loop; note trailing underscore.
