with open("input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip() for line in data]

    def most_of_counter(list):
        num_of_zeroes = 0
        num_of_ones = 0
        for i in range(len(list)):
            if list[i] == "0":
                num_of_zeroes += 1
            if list[i] == "1":
                num_of_ones += 1
        
        if num_of_zeroes == num_of_ones:
            return "eq"
        if num_of_zeroes > num_of_ones:
            return "0"
        if num_of_ones > num_of_zeroes:
            return "1"

    def least_of_counter(list):
        num_of_zeroes = 0
        num_of_ones = 0
        for i in range(len(list)):
            if list[i] == "0":
                num_of_zeroes += 1
            if list[i] == "1":
                num_of_ones += 1
        if num_of_zeroes == num_of_ones:
            return "eq"
        if num_of_zeroes > num_of_ones:
            return "1"
        if num_of_ones > num_of_zeroes:
            return "0"

    def calc_oxygen(data, n):
        if len(data) == 1:
            return data[0]
        n_list = []
        for i in range(len(data)):
            n_list.append((data[i])[n])
        
        if most_of_counter(n_list) == "eq":
            return calc_oxygen([x for x in data if x[n] == "1"], n+1)
        if most_of_counter(n_list) == "0":
            return calc_oxygen([x for x in data if x[n] == "0"], n+1)
        if most_of_counter(n_list) == "1":
            return calc_oxygen([x for x in data if x[n] == "1"], n+1)
    
    def calc_co2(data, n):
        print(data)
        print(n)
        if len(data) == 1:
            return data[0]
        n_list = []
        for i in range(len(data)):
            n_list.append((data[i])[n])

        if least_of_counter(n_list) == "eq":
            return calc_co2([x for x in data if x[n] == "0"], n+1)
        if least_of_counter(n_list) == "0":
            return calc_co2([x for x in data if x[n] == "0"], n+1)
        if least_of_counter(n_list) == "1":
            return calc_co2([x for x in data if x[n] == "1"], n+1)

    bin_oxygen = calc_oxygen(data, 0)
    bin_co2 = calc_co2(data, 0)

    oxygen = int(bin_oxygen, 2)
    co2 = int(bin_co2, 2)

    mult = oxygen*co2


    print("oxygen: {}".format(oxygen))
    print("co2: {}".format(co2))
    print("multiplication {}".format(mult))