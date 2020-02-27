import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill()  # Defaults to white
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, *args, **kwargs):
        self.last_x = None
        self.last_y = None



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
