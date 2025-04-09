import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget

app = QApplication(sys.argv)

class NoteWindow(QWidget):
    def __init__ (self):
        super().__init__()
        self.setWindowFlags(
            self.windowFlags()
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint)
        self.setStyleSheet("background: #FFFF99; color: #62622f; border: 0; font-size: 16pt;")
        layout = QVBoxLayout()
        self.text = QTextEdit()
        layout.addWidget(self.text)
        self.setLayout(layout)

note = NoteWindow()
note.show()
app.exec()