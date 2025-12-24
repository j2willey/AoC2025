import os

def load_data(data_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    banks = []
    with open(data_file_path) as f:
        ranges = []
        ids = []
        range = True
        for line in f:
            if range:
                if line.strip() == "":
                    range = False
                    continue
                ranges.append( [ int(istr) for istr in line.strip().split("-")] )
            else:
                ids.append( int(line.strip()))
    return ranges, ids

def condense_ranges(ranges):
    newranges = []
    # sort ranges by start value
    ranges.sort(key=lambda x: x[0])

    #combine overlapping ranges
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            newranges.append( (current_start, current_end) )
            current_start, current_end = start, end

    newranges.append( (current_start, current_end) )
    return newranges

def is_id_valid(idstr, ranges):
    for start, end in ranges:
        if idstr >= start and idstr <= end:
            return True
    return False

def day05Part1(filename = "input.txt"):
    ranges, ids = load_data(filename)
    condensed_ranges = condense_ranges(ranges)
    fresh_count = 0
    for id in ids:
        if is_id_valid(id, condensed_ranges):
            fresh_count += 1

    return fresh_count, "number of fresh ingredients"

def day05Part2(filename = "input.txt"):

    return "foo", "number of fresh ingredients"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day05Part1(filename)
    part2, desc2 = day05Part2(filename)
    print(f"part 1   {part1} : {desc1} ")
    print(f"part 2   {part2} : {desc2} ")
