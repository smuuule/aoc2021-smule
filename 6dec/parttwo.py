from collections import defaultdict

with open("input.txt", "r") as file:
    data = [int(i) for i in file.read().split(",")]

def count(data, n):
    dict = defaultdict(int)
    for i in data:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1

    for day in range(n):
        curr_dict = defaultdict(int)
        for x, count in dict.items():
            if x == 0:
                curr_dict[6] += count
                curr_dict[8] += count
            else:
                curr_dict[x-1] += count
        dict = curr_dict
    return sum(dict.values())

print(count(data, 256))