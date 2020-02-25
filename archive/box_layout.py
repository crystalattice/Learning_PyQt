import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class GUI(QMainWindow):
    """QMainWindow allows inheritance of widgets not normally available"""

    def __init__(self):
        super().__init__()  # Initialize inherited class to create Window
        self.setWindowTitle("PyQt5 GUI")
        self.resize(400, 300)
        self.init_ui()

    def init_ui(self):
        self.add_menus()
        self.add_statusbar()
        self.box_layout()

    def box_layout(self):
        label_1 = QLabel("First label")
        label_2 = QLabel("Another label")

        button_1 = QPushButton("Click 1")
        button_2 = QPushButton("Click 2")

        hbox_1 = QHBoxLayout()
        hbox_1.addStretch()  # Push/stretch to right
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        vbox = QVBoxLayout()
        vbox.addStretch()  # Push/stretch down
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        layout_widget = QWidget()
        layout_widget.setLayout(vbox)

        self.setCentralWidget(layout_widget)

    def add_menus(self):
        """Add menu items"""
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")

        # Add actions to File menu
        new_icon = QIcon("icons/new_file.png")
        new_action = QAction(new_icon, "New", self)
        new_action.setStatusTip("New File")

        exit_icon = QIcon("icons/exit.png")
        exit_action = QAction(exit_icon, "Exit", self)
        exit_action.setStatusTip("Click to exit application")
        exit_action.triggered.connect(self.close)  # Exit application
        exit_action.setShortcut("Ctrl+Q")  # Reads keyboard strokes

        file_menu.addAction(new_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

    def add_statusbar(self):
        """Add basic status bar"""
        self.statusBar().showMessage("Statusbar text")  # Special widget by virtue of QMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
