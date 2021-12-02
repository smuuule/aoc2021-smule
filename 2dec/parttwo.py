with open("input.txt", "r") as file:
    x, y, aim = 0, 0, 0
    for line in file:
        cmd = line.split()[0]
        val = int(line.split()[1])

        if (cmd == "forward"):
            x += val
            y += aim * val
        
        elif (cmd == "down"):
            aim += val
        
        elif (cmd == "up"):
            aim -= val
    
    print("Cooridnates ({}, {})".format(x, y))
    print("Multiplication: {}".format(x*y))