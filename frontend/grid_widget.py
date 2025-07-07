from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QMouseEvent
from PySide6.QtCore import Qt, QRect
from backend.grid_logic import make_grid, get_constants

ROWS, COLS = get_constants()

class GridWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.cell_size = 50
        self.grid = make_grid()
        self.start = None
        self.end = None
        self.mode = 'start'
        self.path = None
        self.setFixedSize(COLS * self.cell_size, ROWS * self.cell_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        for r in range(ROWS):
            for c in range(COLS):
                node = self.grid[r][c]
                rect = QRect(c*self.cell_size, r*self.cell_size, self.cell_size, self.cell_size)
                color = QColor("#151617")
                if node.is_start:
                    color = QColor("#00C853")
                elif node.is_end:
                    color = QColor("#D50000")
                elif node.is_obstacle:
                    color = QColor("#08233C")
                elif self.path and (r, c) in self.path:
                    color = QColor("#316289")
                painter.fillRect(rect, color)
                painter.setPen(QPen(Qt.gray))
                painter.drawRect(rect)
        if self.path and len(self.path) > 1:
            pen = QPen(QColor("#FFFFFF"), 4)
            painter.setPen(pen)
            for i in range(len(self.path) - 1):
                r1, c1 = self.path[i]
                r2, c2 = self.path[i+1]
                x1 = c1 * self.cell_size + self.cell_size // 2
                y1 = r1 * self.cell_size + self.cell_size // 2
                x2 = c2 * self.cell_size + self.cell_size // 2
                y2 = r2 * self.cell_size + self.cell_size // 2
                painter.drawLine(x1, y1, x2, y2)

    def mousePressEvent(self, event: QMouseEvent):
        c = event.position().x() // self.cell_size
        r = event.position().y() // self.cell_size
        if not (0 <= r < ROWS and 0 <= c < COLS):
            return
        node = self.grid[int(r)][int(c)]
        if self.mode == 'start':
            if self.start:
                self.start.is_start = False
            node.is_start = True
            self.start = node
            self.mode = 'end'
            self.main_window.info.setText("Haz clic para seleccionar el destino")
        elif self.mode == 'end':
            if self.end:
                self.end.is_end = False
            if node == self.start:
                return
            node.is_end = True
            self.end = node
            self.mode = 'obstacle'
            self.main_window.info.setText("Haz clic para agregar obstáculos (haz clic en 'Buscar camino' para terminar)")
            self.main_window.btn_path.setEnabled(True)
        elif self.mode == 'obstacle':
            if node == self.start or node == self.end:
                return
            node.is_obstacle = not node.is_obstacle
        self.path = None
        self.update()

    def reset(self):
        self.grid = make_grid()
        self.start = None
        self.end = None
        self.mode = 'start'
        self.path = None
        self.update()

    def show_path(self, path):
        self.path = path
        self.update()
