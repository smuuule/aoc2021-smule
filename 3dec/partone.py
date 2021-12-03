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
        if num_of_zeroes > num_of_ones:
            return "0"
        if num_of_ones > num_of_zeroes:
            return "1"

    def calc_gamma(data, n):
        gamma = 0
        n_list = []
        for i in range(len(data)):
            n_list.append(data[i][n])
        return most_of_counter(n_list)
    
    def calc_epsilon(gamma):
        inverse_binary = ''.join(['1' if i == '0' else '0'for i in gamma])
        return inverse_binary

    bin_gamma = ''.join([(str(calc_gamma(data, x))) for x in range(12)])
    bin_epsilon = calc_epsilon(bin_gamma)

    gamma = int(bin_gamma, 2)
    epsilon = int(bin_epsilon, 2)

    mult = gamma*epsilon


    print("gamma: {}".format(gamma))
    print("epsilon: {}".format(epsilon))
    print("multiplication {}".format(mult))