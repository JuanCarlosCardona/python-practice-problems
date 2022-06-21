import numpy as np
from queue import PriorityQueue


class Node:
    def __init__(self, cost, row, column):
        self.cost = cost
        self.row = row
        self.column = column
        self.neighbours = []

    def __lt__(self, other):
        return self.cost < other.cost

    def update_neighbours(self, grid, rows):
        if self.column < rows - 1:  # Right
            self.neighbours.append(grid[self.row, self.column + 1])

        if self.column < rows - 1 and self.row > 0:  # Upper Right
            self.neighbours.append(grid[self.row - 1, self.column + 1])

        if self.column < rows - 1 and self.row < rows - 1:  # Down Right
            self.neighbours.append(grid[self.row + 1, self.column + 1])


def dijkstra(source, grid):
    open_nodes = PriorityQueue()
    open_nodes.put(source)
    visited = {source}
    calculated_cost = source.cost
    costs_set = {cost: float('inf') for row in grid for cost in row}
    costs_set[source] = source.cost

    came_from = {}

    while not open_nodes.empty():
        current_node = open_nodes.get()
        visited.remove(current_node)

        if len(current_node.neighbours) == 0:
            break

        for neighbour in current_node.neighbours:
            tmp_cost = costs_set[current_node] + neighbour.cost

            if tmp_cost < costs_set[neighbour]:

                came_from[current_node] = neighbour

                if not visited.__contains__(neighbour):
                    calculated_cost += neighbour.cost
                    costs_set[neighbour] = tmp_cost
                    open_nodes.put(neighbour)
                    visited.add(neighbour)

    return print_path(came_from)


def print_path(came_from):
    result = 0
    for previous, current in came_from.items():
        print(f'Cost {previous.cost} : Row {previous.row} : Column {previous.column} -> Cost {current.cost} : '
              f'Row {current.row} : Column {current.column}')
        result += previous.cost

    return result


gold = np.array([[Node(1, 0, 0), Node(3, 0, 1), Node(1, 0, 2), Node(5, 0, 3)],
                 [Node(2, 1, 0), Node(2, 1, 1), Node(4, 1, 2), Node(1, 1, 3)],
                 [Node(5, 2, 0), Node(0, 2, 1), Node(2, 2, 2), Node(3, 2, 3)],
                 [Node(0, 3, 0), Node(6, 3, 1), Node(1, 3, 2), Node(2, 3, 3)]], dtype='O')

total_rows, total_columns = gold.shape

gold_list = gold.tolist()

for i in range(total_rows):
    for j in range(total_columns):
        node = gold_list[i][j]
        node.update_neighbours(gold, total_rows)

max_coins = dijkstra(gold[2, 0], gold)
print(f'Result : {max_coins}')
