with open("input.txt", "r") as file:
    x, y = 0, 0
    for line in file:
        cmd = line.split()[0]
        val = int(line.split()[1])

        if (cmd == "forward"):
            x += val
        
        elif (cmd == "down"):
            y += val
        
        elif (cmd == "up"):
            y -= val
    
    print("Cooridnates ({}, {})".format(x, y))
    print("Multiplication: {}".format(x*y))