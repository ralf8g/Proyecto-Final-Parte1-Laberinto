from PySide6.QtWidgets import QApplication
from frontend.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

