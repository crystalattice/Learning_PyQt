import sys  # For command line arguments

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CustomDialog(QDialog):
    """Subclass modal dialog box"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("HELLO!")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.button_box = QDialogButtonBox(QBtn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    """Subclass QMainWindow to customize application's main window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My awesome app")
        label = QLabel("This is awesome!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)  # Set central widget; allows expansion to fill entire window by default.

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("android.png"), "Your button", self)  # Define the action for the button;
        # button can be text and/or icon
        button_action.setStatusTip("This is your button")  # Tooltip
        button_action.triggered.connect(self.toolbar_click)  # Link button to method
        button_action.setCheckable(True)  # Set button as togglable
        button_action.setShortcut(QKeySequence("Ctrl+p"))  # You can enter keyboard shortcuts using key names (e.g.
        # Ctrl+p), Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P), or system agnostic identifiers
        # (e.g. QKeySequence.Print)
        toolbar.addAction(button_action)  # Add button to toolbar

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("android.png"), "Your button2", self)
        button_action2.setStatusTip("This is the second button")
        button_action2.triggered.connect(self.toolbar_click)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))  # Captures tooltip and displays on status bar

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)  # Use the existing button from the toolbar
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")  # Submenu of parent menu
        file_submenu.addAction(button_action2)

    def toolbar_click(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success")
        else:
            print("Cancel!")


app = QApplication(sys.argv)  # Runs event loop; set to capture CLI arguments. To ignore CLI args, use QApplication([]).

window = MainWindow()
window.show()  # Required to display windows; invisible by default.

app.exec_()  # Start event loop; note trailing underscore.
