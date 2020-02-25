import sys

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # Create application
win = QWidget()  # Create window

# Set properties
win.setWindowTitle("PyQt5 GUI")  # Set window title
win.resize(400, 300)  # Width, height

win.show()  # Display window

# Execute application
sys.exit(app.exec_())  # Ending underscore signifies Qt exec() call, not base Python exec() call; sys.exit() ensures
# errors are captured by Python
