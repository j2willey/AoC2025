import os
import itertools

def load_data(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)
    points = []

    with open(data_file_path) as f:
        for line in f:
            points.append([ int(s) for s in line.split(',')])

    # for i, p in enumerate(points):
    #     if i <= 20:
    #         print(f"{i} {p}")

    return points


def day10Part1(filename = "input.txt"):

    return "foo", "Part 1 result"


def day10Part2(filename = "input.txt"):

    return "bar", "Part 2 result"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day10Part1(filename)
    part2, desc2 = day10Part2(filename)
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

