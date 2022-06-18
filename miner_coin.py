import numpy as np


class Node:
    def __init__(self, weight, row, column):
        self.weight = weight
        self.row = row
        self.column = column
        self.neighbours = []

    def get_weight(self):
        return self.weight

    def update_neighbours(self, grid, total_rows, total_columns):

        if self.column < total_rows:
            for value in np.nditer(grid[self.row][self.column:]):
                self.neighbours.append(value)


gold = np.array([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]])

total_rows, total_columns = gold.shape

print(gold)
print(gold.diagonal())
print(np.flipud(gold).diagonal())

sub_arr = gold[1:].diagonal()

print(sub_arr)
