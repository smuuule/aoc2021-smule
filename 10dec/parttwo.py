import statistics

with open("input.txt") as file:
    data = file.read().splitlines()
    points = []
    for line in data:
        list = []
        for i in line:
            if i in ['(', '[', '{', '<']:
                list.append(i)
            elif i == ')':
                if list[-1] == '(':
                    list.pop()
                else:
                    break

            elif i == ']':
                if list[-1] == '[':
                    list.pop()
                else:
                    break

            elif i == '}':
                if list[-1] == '{':
                    list.pop()
                else:
                    break

            elif i == '>':
                if list[-1] == '<':
                    list.pop()
                else:
                    break
        else:
            count = 0
            for i in reversed(list):
                count *= 5
                if i == '(':
                    count += 1
                elif i == '[':
                    count += 2
                elif i == '{':
                    count += 3
                elif i == '<':
                    count += 4
            points.append(count)

print(statistics.median(points))