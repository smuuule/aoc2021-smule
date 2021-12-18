import collections

with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

initial = data[0]
dict = {}
for rule in data[2:]:
    first, second = rule.split(" -> ")
    dict[first] = second

for i in range(40):
    result = ""
    for j in range(len(initial)-1):

        print(len(initial))
        pair = initial[j:j+2]
        if pair in dict:
            result += pair[0] + dict[pair]
        else:
            result += pair

    result += initial[-1]
    initial = result

    print("{}: {}".format(i, result))

most = collections.Counter(result).most_common()[0][1]
least = collections.Counter(result).most_common()[-1][1]

print("Answer: " + str(most - least))