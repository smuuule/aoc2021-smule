from __future__ import annotations
import collections

with open("input.txt") as file:
    data = file.readlines()

points: collections.Counter[tuple[int, int]] = collections.Counter()

for line in data:
    first, second = line.split(' -> ')
    x1, y1 = first.split(',')
    x2, y2 = second.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Vertical
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, i)] +=1
    # Horizontal
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            points[(i, y1)] +=1
    # Diagon Alley
    else:
        if x1 < x2:
            xdiff = 1
        else:
            xdiff = -1
        if y1 < y2:
            ydiff = 1
        else:
            ydiff = -1

        x, y = x1, y1
        while (x, y) != (x2 + xdiff, y2 + ydiff):
            points[(x, y)] += 1
            x, y = x + xdiff, y + ydiff

count = 0
for i, j in points.most_common():
    if j > 1:
        count += 1
    else:
        break

print("count: " + str(count))