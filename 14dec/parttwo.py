import collections

with open("input.txt", "r") as file:
    data = file.read()

initial, rules = data.split('\n\n')

counts = collections.Counter()
for i in range(0, len(initial) - 1):
    counts[initial[i:i + 2]] += 1

patterns = {}
for line in rules.splitlines():
    in_p, ins = line.split(' -> ')
    patterns[in_p] = ins

for i in range(40):
    counts2 = collections.Counter()
    new_counts = collections.Counter()
    for i, j in counts.items():
        new_counts[f'{i[0]}{patterns[i]}'] += j
        new_counts[f'{patterns[i]}{i[1]}'] += j
        counts2[i[0]] += j
        counts2[patterns[i]] += j
    counts = new_counts

counts2[initial[-1]] += 1

s_counts = sorted(v for v in counts2.values())
print("Answer: " + str(s_counts[-1] - s_counts[0]))