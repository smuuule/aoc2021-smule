with open("input.txt", "r") as file:
    data = [int(i) for i in file.read().split(",")]

def calc_new_data(data):
    new_fish = 0
    for inx, i in enumerate(data):
        if i == 0:
            data[inx] = 7
            new_fish += 1
    new = [x-1 for x in data]
    for i in range(new_fish):
        new.append(8)
    return new

def count_fish(data, n):
        for i in range(n):
            print(i)
            data = calc_new_data(data)
        return len(data)

print(count_fish(data, 256))