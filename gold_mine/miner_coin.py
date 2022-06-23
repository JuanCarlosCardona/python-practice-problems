# Given a gold mine of n*m dimensions. Each field in this mine contains a
# positive integer which is the amount of gold in tons. Initially the miner is at
# first column but can be at any row. He can move only (right->,right up /,right
# down\) that is from a given cell, the miner can move to the cell diagonally up
# towards the right or right or diagonally down towards the right.
# Find out maximum amount of gold he can collect.


import numpy as np
from queue import PriorityQueue


class Node:
    def __init__(self, cost, row, column, came_from=None):
        self.cost = cost
        self.row = row
        self.column = column
        self.neighbours = []
        self.came_from = came_from

    def __gt__(self, other):
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
    costs_set = {cost: float('inf') for row in grid for cost in row}  # initialize all nodes to +inf
    costs_set[source] = source.cost

    while not open_nodes.empty():
        current_node = open_nodes.get()
        visited.remove(current_node)

        if len(current_node.neighbours) == 0:   # Base case
            return get_result(current_node)

        for neighbour in current_node.neighbours:
            tmp_cost = costs_set[current_node] + neighbour.cost

            if tmp_cost < costs_set[neighbour]:

                neighbour.came_from = current_node

                if not visited.__contains__(neighbour):
                    costs_set[neighbour] = tmp_cost
                    open_nodes.put(neighbour)
                    visited.add(neighbour)

    return 0


def get_result(current):
    result = 0
    path = []

    # Append the path from end to origin and get the sum of the weights of each node
    while not (current is None):
        path.append(current)
        result += current.cost
        current = current.came_from

    reversed_path = path[::-1]  # Order path from origin to end

    for node in reversed_path:
        print(f'Node( Cost {node.cost} : Row {node.row} : Column {node.column}) ->', end=' ')

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
