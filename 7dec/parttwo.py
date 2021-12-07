with open("input.txt", "r") as file:
    data = [int(i) for i in file.read().split(",")]

fuels = {}
for i in range(max(data)):
    curr_fuel = 0
    for pos in data:
        curr_fuel += (abs(i - pos) ** 2 + abs(i - pos)) // 2
    fuels[i] = curr_fuel
position = min(fuels, key=fuels.get)
least_fuel = min(fuels.values())


print(f"Poisition: {position}\t Least Fuel: {least_fuel}")