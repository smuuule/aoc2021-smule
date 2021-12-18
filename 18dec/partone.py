import re

def adder(first, second):
    return "[" + first + "," + second + "]"

def reduce(line):
    while True:
        con = False
        for pair in pairs.finditer(line):
            print(pair)
        

def magnitude(line):
    return 0

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

pairs = re.compile(r'\[(\d+), (\d+)\]')


print(reduce(lines[0]))

print(adder("[1,2]", "[[3,4],5]"))

# ight imma head out