import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLabel, QPushButton


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
        self.grid_layout()

    def grid_layout(self):
        label_1 = QLabel("First label")
        label_2 = QLabel("Another label")

        button_1 = QPushButton("Click 1")
        button_2 = QPushButton("Click 2")

        grid = QGridLayout()
        grid.addWidget(label_1, 0, 0)
        grid.addWidget(button_1, 0, 1)
        grid.addWidget(label_2, 1, 0)
        grid.addWidget(button_2, 1, 1)
        grid.setAlignment(Qt.AlignBottom)

        layout_widget = QWidget()
        layout_widget.setLayout(grid)
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
