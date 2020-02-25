import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class GUI(QMainWindow):
    """QMainWindow allows inheritance of widgets not normally available"""
    def __init__(self):
        super().__init__()  # Initialize inherited class to create Window
        self.init_ui()  # Refer to Window as "self"

    def init_ui(self):
        """Set properties and add widgets"""
        self.setWindowTitle("PyQt5 GUI")
        self.resize(400, 300)
        self.add_menus()
        self.add_statusbar()

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
