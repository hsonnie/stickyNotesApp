import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
from PySide6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__ ()

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)
class Color(QWidget):
        def __init__ (self, color):
            super ().__init__ ()
            self.ser=tAutoFillBackground(True)
            
            palette = self.palette()
            palette.setColor(QPalette.ColorRole.window, QColor(color))
            self.setPalette(palette)
app = QApplication()
window = MainWindow()
window.show()
app.exec()