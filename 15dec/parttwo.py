from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open("input.txt", "r") as file:
    data = [ []*100 for i in range(100)]
    for index, line in enumerate(file.readlines()):
        for i in line.strip():
            data[index].append(int(i))


def expand(risk_map: list[list[int]], repeat: int) -> list[list[int]]:
    new_map = []
    for y in range(repeat):
        for line in risk_map:
            new_map.append([])
            for x in range(repeat):
                new_map[-1] += [(field + x + y - 1) % 9 + 1 for field in line]
    return new_map

data = expand(data, 5)

grid = Grid(matrix=data)

start = grid.node(0, 0)
end = grid.node(499, 499)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

risk = 0
for x, y in path[1:]:
    risk += int(data[y][x])

print('operations:', runs, 'path length:', len(path), 'total risk:', risk)