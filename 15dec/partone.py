from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open("input.txt", "r") as file:
    data = [ []*100 for i in range(100)]
    for index, line in enumerate(file.readlines()):
        for i in line.strip():
            data[index].append(i)

grid = Grid(matrix=data)

start = grid.node(0, 0)
end = grid.node(99, 99)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

risk = 0
for x, y in path[1:]:
    risk += int(data[y][x])

print('operations:', runs, 'path length:', len(path), 'total risk:', risk)
print(grid.grid_str(path=path, start=start, end=end))