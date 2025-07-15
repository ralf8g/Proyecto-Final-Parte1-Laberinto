from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from frontend.grid_widget import GridWidget
from backend.astar import astar
from backend.grid_logic import agregar_obstaculos_aleatorios
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        fuente = QFont("Georgia", 10, QFont.Weight.Light)
        self.setWindowTitle("Algoritmo A*")
        self.grid_widget = GridWidget(self)
        self.info = QLabel("Haz clic para seleccionar el inicio")
        self.info.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: white;
                background-color: #3498db;
                padding: 10px;
                border-radius: 15px;
            }
        """)
        self.btn_path = QPushButton("Buscar camino")
        self.btn_path.setFixedSize(300,50)
        self.btn_path.setFont(fuente)
        self.btn_path.setEnabled(False)
        self.btn_path.clicked.connect(self.run_astar)
        self.btn_reset = QPushButton("Reiniciar")
        self.btn_reset.setFixedSize(300,50)
        self.btn_reset.setFont(fuente)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_obstaculos = QPushButton("Obstáculos aleatorios")
        self.btn_obstaculos.setFixedSize(300,50)
        self.btn_obstaculos.setFont(fuente)
        self.btn_obstaculos.clicked.connect(self.generar_obstaculos)
        layout = QVBoxLayout()
        layout.addWidget(self.grid_widget)
        layout.addWidget(self.info)
        layout.addWidget(self.btn_path,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_reset,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_obstaculos,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setSpacing(5)
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

    def generar_obstaculos(self):
        if not self.grid_widget.start or not self.grid_widget.end:
            QMessageBox.warning(self, "Advertencia", "Primero debes seleccionar inicio y fin.")
            return

        cantidad = 30
        agregar_obstaculos_aleatorios(self.grid_widget.grid, cantidad)
        self.grid_widget.update()
        self.info.setText("Obstáculos aleatorios generados.")


