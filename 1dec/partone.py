with open("input.txt", "r") as file:
  count = 0
  for line in file:
    curr = int(line.strip())
    if ("prev" in locals()): 
        if (prev < curr):
            count += 1
    prev = curr
  print("count: " + str(count))