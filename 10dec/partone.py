with open("input.txt") as file:
    data = file.read().splitlines()
    count = 0
    for line in data:
        print(line)
        list = []
        for i in line:
            if i in ['(', '[', '{', '<']:
                list.append(i)
            elif i == ')':
                if list[-1] == '(':
                    list.pop()
                else:
                    count += 3
                    broke = True
                    break

            elif i == ']':
                if list[-1] == '[':
                    list.pop()
                else:
                    count += 57
                    broke = True
                    break

            elif i == '}':
                if list[-1] == '{':
                    list.pop()
                else:
                    count += 1197
                    broke = True
                    break

            elif i == '>':
                if list[-1] == '<':
                    list.pop()
                else:
                    count += 25137
                    broke = True
                    break
        
print(count)