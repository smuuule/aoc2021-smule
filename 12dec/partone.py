from collections import defaultdict

with open("input.txt", "r") as file:
    data = file.read().splitlines()

nodes = defaultdict(set)
for line in data:
    first, second = line.split('-')
    nodes[first].add(second)
    nodes[second].add(first)

done = set()

rest: list = [(('start',), False)]
while rest:
    path, small = rest.pop()
    if path[-1] == 'end':
        done.add(path)
        continue

    for way in nodes[path[-1]] - {'start'}:
        if way.isupper():
            rest.append(((*path, way), small))
        elif small is False and path.count(way) == 1:
            rest.append(((*path, way), True))
        elif way not in path:
            rest.append(((*path, way), small))

print(len(done))