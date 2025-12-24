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

def find_max_bank_by_count(bank: str, count: int) -> int:
    ibank = [int(c) for c in bank]
    n = len(ibank)
    if count <= 0:
        return 0
    if count > n:
        raise ValueError("count cannot exceed bank length")

    idx = 0
    joltage = 0
    for digit in range(count):
        remaining = count - digit - 1
        # end is exclusive index: we must leave room for `remaining` digits after the pick
        end = n - remaining
        # choose maximum digit in ibank[idx:end]
        best_digit = max(ibank[idx:end])
        # find its index within the allowed window and add 1
        idx = ibank.index(best_digit, idx, end) + 1
        joltage = joltage * 10 + best_digit
    return joltage


def day03Part1(filename = "input.txt"):
    joltage = 0
    banks = load_data(filename)
    for bank in banks:
        joltage += find_max_bank_by_count(bank, 2)
    return joltage, "joltage"

def day03Part2(filename = "input.txt"):
    joltage = 0
    banks = load_data(filename)
    for bank in banks:
        joltage += find_max_bank_by_count(bank, 12)
    return joltage, "joltage"

if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day03Part1(filename)
    part2, desc2 = day03Part2(filename)
    print(f"part 1   {part1} : {desc1} ")
    print(f"part 2   {part2} : {desc2} ")
