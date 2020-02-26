import sys  # For command line arguments

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    """Subclass QMainWindow to customize application's main window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My awesome app")
        layout = QVBoxLayout()
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)  # Runs event loop; set to capture CLI arguments. To ignore CLI args, use QApplication([]).

window = MainWindow()
window.show()  # Required to display windows; invisible by default.

app.exec_()  # Start event loop; note trailing underscore.
