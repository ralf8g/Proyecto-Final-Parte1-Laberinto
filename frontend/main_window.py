from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from frontend.grid_widget import GridWidget
from backend.astar import astar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algoritmo A*")
        self.grid_widget = GridWidget(self)
        self.info = QLabel("Haz clic para seleccionar el inicio")
        self.btn_path = QPushButton("Buscar camino")
        self.btn_path.setEnabled(False)
        self.btn_path.clicked.connect(self.run_astar)
        self.btn_reset = QPushButton("Reiniciar")
        self.btn_reset.clicked.connect(self.reset)
        layout = QVBoxLayout()
        layout.addWidget(self.grid_widget)
        layout.addWidget(self.info)
        layout.addWidget(self.btn_path)
        layout.addWidget(self.btn_reset)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_astar(self):
        if not self.grid_widget.start or not self.grid_widget.end:
            QMessageBox.information(self, "Error", "Debes seleccionar inicio y destino.")
            return
        path,costo = astar(self.grid_widget.grid, self.grid_widget.start, self.grid_widget.end)
        if path:
            self.grid_widget.show_path(path)
            self.info.setText(f"¡Camino encontrado! Costo: {costo}")
        else:
            self.info.setText("No hay camino posible.")
            QMessageBox.information(self, "Sin camino", "No hay camino posible.")

    def reset(self):
        self.grid_widget.reset()
        self.info.setText("Haz clic para seleccionar el inicio")
        self.btn_path.setEnabled(False)
