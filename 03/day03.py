import os
from itertools import product

def load_data(data_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    banks = []
    with open(data_file_path) as f:
        for line in f:
            banks.append( line.strip())
    return banks

def day02Part1(filename = "input.txt"):
    joltage = 0
    banks = load_data(filename)
    for bank in banks:
        ibank = [int(c) for c in bank]
        d1 = max(ibank[:-1])
        d2 = 0
        i1 = bank.index(str(d1))
        if i1 == len(bank) -1:
            d2 = max(ibank[:-1])
            d1 = max(ibank[:-2])
        else:
            d2 = max(ibank[i1+1:])
        joltage += (d1 * 10) + d2
    return joltage, "joltage"

if __name__ == "__main__":
    filename = "input.txt"
    part1, desc1 = day02Part1(filename)
    # part2, desc2 = day02Part2(filename)
    print(f"part 1   {part1} : {desc1} ")
    # print(f"part 2   {part2} : {desc2} ")
