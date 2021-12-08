from collections import defaultdict

"""
We know that:
    Displays with 2 inputs results in a '1'
    Displays with 4 inputs results in a '4'
    Displays with 3 inputs results in a '7'
    Displays with 7 inputs results in a '8'
    {GROUP A}

    Displays with 5 inputs results in a '2, 3 or 5' {GROUP B}
    Displays with 6 inputs results in a '6 or 9' {GROUP C}
"""

with open("input.txt") as file:
    data = file.read().strip().split('\n')
    group_a = {2: 1, 4: 4, 3: 7, 7: 8}
    group_a_count = 0
    total = 0
    for line in data:
        parts = [x.strip() for x in line.split('|')]
        input, output = [set(p) for p in parts[0].split()], [set(p) for p in parts[1].split()]
        output_sum = 0
        numbers = [set()] * 10
        displays = [''] * 7
        group_b, group_c = [], []
        for i in input:
            if len(i) in group_a:
                numbers[group_a[len(i)]] = i
            elif len(i) == 5:
                group_b.append(i)
            else:
                group_c.append(i)
        displays[0] = numbers[7].difference(numbers[1]).pop()
        union_13 = numbers[4].difference(numbers[1])
        union_0156 = group_c[0].intersection(group_c[1]).intersection(group_c[2])
        displays[3] = union_13.union(displays[0]).difference(union_0156).pop()
        displays[1] = union_13.difference(displays[3]).pop()
        numbers[0] = next(filter(lambda s: displays[3] not in s, group_c))
        union_4_6 = numbers[0].difference(numbers[1]).difference(displays[0], displays[1])
        displays[4] = union_4_6.difference(union_0156).pop()
        numbers[9] = next(filter(lambda s: displays[4] not in s, group_c))
        numbers[6] = next(filter(lambda s: s != numbers[0] and s != numbers[9], group_c))
        numbers[3] = numbers[9].difference(displays[1])
        numbers[5] = numbers[6].difference(displays[4])
        numbers[2] = next(filter(lambda s: s != numbers[3] and s != numbers[5], group_b))

        for index, s in enumerate(output):
                    if len(s) in group_a:
                        group_a_count += 1
                    factor = 10**(3-index)
                    for num, d in enumerate(numbers):
                        if d == s:
                            output_sum += factor * num
                            break
        total += output_sum
print(group_a)
print(total)
