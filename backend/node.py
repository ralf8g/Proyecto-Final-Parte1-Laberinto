class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_obstacle = False
        self.is_start = False
        self.is_end = False

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))
