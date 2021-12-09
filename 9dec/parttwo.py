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

basinSizes = []
prev = set()
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if(row, col) not in prev and arr[row][col] != 9:
            size = 0
            tmp = []
            tmp.append((row, col))
            while len(tmp) != 0:
                (row, col) = tmp[0]
                del tmp[0]
                if (row, col) in prev:
                    continue
                prev.add((row, col))
                size += 1
                for i in range(4):
                    coordRow = row+adjRow[i]
                    coordCol = col+adjCol[i]
                    if 0 <= coordRow < len(arr) and 0 <= coordCol < len(arr):
                        if arr[coordRow][coordCol] != 9:
                            tmp.append((coordRow, coordCol))
            basinSizes.append(size)
basinSizes.sort()
print(basinSizes[-1]*basinSizes[-2]*basinSizes[-3])
                        
