with open("input.txt", "r") as file:
  count = 0
  for line in file:
    next = int(line.strip())
    
    if ("second" in locals()):
        third = second
    if ("first" in locals()):
        second = first
    first = next
    if (("first" in locals()) and ("second" in locals()) and ("third" in locals())):
        if ("sum" in locals()):
            if ((first + second + third) > sum):
                count += 1
        sum = first + second + third
  print("count: " + str(count))