from .node import Node

ROWS, COLS = 14,14

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
