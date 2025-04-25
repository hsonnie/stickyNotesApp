import sys 
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, 
    QWidget, QLineEdit, QPushButton,
    )
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wolfram Father")

        self.input = QLineEdit()
        self.input.setPlaceholderText("enter a function in x, e.g.: x**2-3*x ")

        self.button = QPushButton("Draw")
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.button.clicked.connect(self.plot)

    def plot(self):
        expretion = self.input.text()
        x = np.linspace(-10, 10, 400)

        try:
            y = eval(expretion, {"x": x, "np": np, "__bulltins__": {}})
        except Exception as e:
            print("Invalid function:", e)
            return
        
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x,y)
        ax.set_title(f"y = {expretion}")
        self.canvas.draw()


app = QApplication(sys.argv)
window = PlotWindow()
window.show()
sys.exit(app.exec())

