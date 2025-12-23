import os
import itertools
from itertools import product

def load_data(data_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    valid_ranges = []
    with open(data_file_path) as f:
        for line in f:
            for idrange in line.strip().split(','):
                istart, iend = idrange.split('-')
                valid_ranges.append( ((istart), (iend)) )
    return valid_ranges

def day02Part1(filename = "input.txt"):
    global __day2Part1
    ranges = load_data(filename)

    # collect invalid ids in a set so overlapping ranges don't double-count
    invalid_ids = set()

    for start, end in ranges:
        istart = int(start)
        iend = int(end)
        startlen = len(start)
        endlen = len(end)

        if startlen % 2 == 1:
            startlen += 1
        if startlen > endlen:
            continue
        for length in range(startlen, endlen + 1, 2):
            halves = product('0123456789', repeat = length // 2)
            for half in halves:
                if half[0] == '0':
                    continue
                fullstr = ''.join(half + half)
                fullid = int(fullstr)
                if fullid >= istart and fullid <= iend:
                    invalid_ids.add(fullid)

    invalid_idsum = sum(invalid_ids)
    return invalid_idsum, "invalid IDs sum"

def day02Part2(filename = "input.txt"):
    global __day2Part2
    ranges = load_data(filename)

    # collect invalid ids in a set so overlapping ranges don't double-count
    invalid_ids = set()

    for start, end in ranges:
        istart = int(start)
        iend = int(end)
        startlen = len(start)
        endlen = len(end)
        # if startlen % 2 == 1:
        #     startlen += 1
        if startlen > endlen:
            continue
        for length in range(startlen, endlen + 1):
            for p in (2,3,4,5,6,7,8,9,10,11,13,17,19):
                if p > 2 and length // p < 1:
                    break
                if length % p != 0:
                    continue

                parts = product('0123456789', repeat = length // p)
                for part in parts:
                    if part[0] == '0':
                        continue
                    fullstr = ''.join(part * p)
                    fullid = int(fullstr)
                    if fullid >= istart and fullid <= iend:
                        # print(f"  id {fullstr}", end=' ')
                        invalid_ids.add(fullid)

    invalid_idsum = sum(invalid_ids)
    return invalid_idsum, "invalid IDs sum"

if __name__ == "__main__":
    filename = "input.txt"
    part1, desc1 = day02Part1(filename)
    part2, desc2 = day02Part2(filename)
    print(f"part 1   {part1} : {desc1} ")
    print(f"part 2   {part2} : {desc2} ")
