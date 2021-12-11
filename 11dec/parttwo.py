from typing import Generator

with open("input.txt", "r") as file:
    data = file.read().splitlines()

def sides(inX: int, inY: int) -> Generator[tuple, None, None]:
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue
            yield inX + x, inY + y

coords = {}
for y, rest in enumerate(data):
    for x, p in enumerate(rest):
        coords[(x, y)] = int(p)


count = 0
while True:
    count += 1
    willFlash = []
    for octo in coords:
        coords[octo] += 1
        if coords[octo] > 9:
            willFlash.append(octo)

    while willFlash:
        nextFlash = willFlash.pop()
        if coords[nextFlash] == 0:
            continue
        coords[nextFlash] = 0
        for octo in sides(*nextFlash):
            if octo in coords and coords[octo] != 0:
                coords[octo] += 1
                if coords[octo] > 9:
                    willFlash.append(octo)

    if all(val == 0 for val in coords.values()):
        print(count)
        break