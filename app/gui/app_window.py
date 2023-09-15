import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import design
import mylib

class AppWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.computeButton.clicked.connect(self.on_compute)

    def on_compute(self):
        x = float(self.inputField.text())
        result = mylib.compute(x)
        self.resultLabel.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
