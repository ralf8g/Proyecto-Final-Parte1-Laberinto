import math
from .grid_logic import get_neighbors


def heuristic(a, b):
    return math.sqrt((a.row - b.row) ** 2 + (a.col - b.col) ** 2)

def astar(grid, start, end):
    open_set = set([start])
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = min(open_set, key=lambda n: f_score.get(n, float('inf')))
        if current == end:
            path = []
            while current in came_from:
                path.append((current.row, current.col))
                current = came_from[current]
            path.append((start.row, start.col))
            return path[::-1], g_score[end]
        open_set.remove(current)
        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                if neighbor not in open_set:
                    open_set.add(neighbor)
    return None, float('inf')


def calcular_costo_camino(path):
    if path is None:
        return float('inf') 
    return len(path) - 1  
