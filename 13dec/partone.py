with open("input.txt", "r") as file:
    data = file.read()

coords = set()

points, folds = data.split("\n\n")

for line in points.splitlines():
    x, y = line.split(',')
    coords.add((int(x), int(y)))

for line in folds.splitlines():
    first, second = line.split('=')
    dir = first[-1]
    val = int(second)

    if dir == 'x':
        coords = {
            (x if x < val else val - (x - val), y) for x, y in coords
        }
    else:
        coords = {
            (x, y if y < val else val - (y - val)) for x, y in coords
        }

    break

print(len(coords))