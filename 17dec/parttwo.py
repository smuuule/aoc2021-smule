with open("input.txt", "r") as file:
    inputStr = file.read()

_, _, x, y = inputStr.split()
x = x[2:-1]
y = y[2:]

x1_tmp, x2_tmp = x.split('..')
y1_tmp, y2_tmp = y.split('..')

x1, x2 = int(x1_tmp), int(x2_tmp)
y1, y2 = int(y1_tmp), int(y2_tmp)

count = 0
for x in range(1, x2 + 1):
    for y in range(y1, abs(y1)):
        x_vel, y_vel = x, y
        x_pos, y_pos = 0, 0
        for i in range(2 * abs(y1) + 1):
            x_pos += x_vel
            y_pos += y_vel
            x_vel = max(x_vel - 1, 0)
            y_vel -= 1

            if y1 <= y_pos <= y2 and x1 <= x_pos <= x2:
                count += 1
                break
            elif y_pos < y1 or x_pos > x2:
                break

print('total:', count)