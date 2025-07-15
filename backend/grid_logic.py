from .node import Node
import random

ROWS, COLS = 12,30

def make_grid():
    return [[Node(r, c) for c in range(COLS)] for r in range(ROWS)]

def get_neighbors(node, grid):
    neighbors = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = node.row + dr, node.col + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and not grid[nr][nc].is_obstacle:
            neighbors.append(grid[nr][nc])
    return neighbors

def get_constants():
    return ROWS, COLS

def agregar_obstaculos_aleatorios(grid, cantidad):
    filas = len(grid)
    columnas = len(grid[0]) if filas > 0 else 0
    colocados = 0

    while colocados < cantidad:
        r = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)
        nodo = grid[r][c]
        if not nodo.is_start and not nodo.is_end and not nodo.is_obstacle:
            nodo.is_obstacle = True
            colocados += 1
