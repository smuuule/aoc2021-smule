with open("input.txt", "r") as file:
    arr = []
    for line in file:
        arr.append([int(i) for i in list(line.strip())])

count = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        low_point = True
        adjRow = [-1, 0, 1, 0]
        adjCol = [0, 1, 0, -1]
        for i in range(4):
            coordRow = row+adjRow[i]
            coordCol = col+adjCol[i]
            if 0 <= coordRow < len(arr) and 0 <= coordCol < len(arr):
                if arr[coordRow][coordCol] <= arr[row][col]:
                    low_point = False
        if low_point:
            count += arr[row][col]+1
print("count: " + str(count))
