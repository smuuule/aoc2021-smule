import sys
import re

with open ("input.txt", "r") as file:
    dataHex = file.read()

def hexToBin(str):
    hexList = re.findall('..', str)
    newHex = []
    for hex in hexList:
        newHex.append(bin(int(hex, 16))[2:].zfill(8))
    newHex = ('').join(newHex)

    return newHex

def binToDec(bin):
    return int(bin, 2)

def calc_packet(packet):
    print(packet)

    v = binToDec(packet[:3])
    t = binToDec(packet[3:6])
    print("v: {}\nt: {}".format(v, t))

    if t == 4:
        groups = []
        whole, rest = divmod(len(packet[6:]), 5)
        for inx in range(whole):
            groups.append(packet[6+inx*5:11+inx*5])

        literals = []
        for group in groups:
            if group[0] == "1":
                literals.append(group[1:])
            if group[0] == "0":
                literals.append(group[1:])
                break
        
        return binToDec(''.join(literals))

    else:
        i = binToDec(packet[6])
        print("i:", i)
        groups = []
        if i == 0:
            l = binToDec(packet[6:22])
            print("l:", l)
            whole, rest = divmod(l, 11)
            for inx in range(whole-1):
                groups.append(packet[22+inx*11:33+inx*11])
            if whole == 0:
                groups.append(packet[22:22+rest])
            else:
                groups.append(packet[22+(whole-1)*11:33+(whole-1)*11+rest])
        elif i == 1:
            l = binToDec(packet[7:18])
            print("l:", l)
            for inx in range(l):
                groups.append(packet[18+inx*11:29+inx*11])
        else:
            print("ERROR: Invalid length type ID!")
            sys.exit(5)

        print(groups)

        return sum([calc_packet(group) for group in groups])
    
print(calc_packet(hexToBin("8A004A801A8002F478")))