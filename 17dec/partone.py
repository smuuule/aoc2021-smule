with open("input.txt", "r") as file:
    inputStr = file.read()

_, _, x, y = inputStr.split()
x = x[2:-1]
y = y[2:]

y1, _ = y.split('..')

y0 = abs(int(y1)) - 1

quickMaths = pow(y0, 2) - (y0 - 1) * y0 // 2

print(quickMaths)