import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget

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

        buttons = QHBoxLayout()
        self.close_btn = QPushButton("x")
        self.close_btn.setStyleSheet("font-weight: bold; font-size: 25px; width: 25px: hight: 25px;")
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.clicked.connect(self.close)
        buttons.addStretch()
        buttons.addWigdet(self.close_btn)
        layout.addLayout(buttons)

        self.text = QTextEdit()
        layout.addWidget(self.text)
        self.setLayout(layout)

note = NoteWindow()
note.show()
app.exec()

