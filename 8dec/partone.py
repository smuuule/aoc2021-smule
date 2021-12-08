from collections import defaultdict

"""
We know that:
    Displays with 2 inputs results in a '1'
    Displays with 4 inputs results in a '4'
    Displays with 3 inputs results in a '7'
    Displays with 7 inputs results in a '8'

    Displays with 5 inputs results in a '2, 3 or 5'
    Displays with 6 inputs results in a '6 or 9'
"""

with open("input.txt") as file:
    count = 0
    for line in file:
        input, output = line.split('|')
        input = input.split()
        output = output.split()
        x = defaultdict(list)
        for i in input:
            x[len(i)].append(i)
            print(x)
        for i in output:
            if len(x[len(i)]) == 1:
                count += 1

print(count)
