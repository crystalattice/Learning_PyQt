import sys  # For command line arguments

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    """Subclass QMainWindow to customize application's main window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My awesome app")

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        # for n, color in enumerate(["red", "green", "blue", "yellow"]):
        #     tabs.addTab(Color(color), color)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)  # Set central widget; allows expansion to fill entire window by default.


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)  # Runs event loop; set to capture CLI arguments. To ignore CLI args, use QApplication([]).

window = MainWindow()
window.show()  # Required to display windows; invisible by default.

app.exec_()  # Start event loop; note trailing underscore.
