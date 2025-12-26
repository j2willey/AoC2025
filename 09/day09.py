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


def day09Part1(filename = "input.txt"):
    global __day8Part1
    points = load_data(filename)
    maxrec = max( [abs(x1-x2+1) * abs(y1-y2+1) for (x1,y1),(x2,y2) in (itertools.combinations(points, 2)) ] )

    return maxrec, "max rectangle area"


def day09Part2(filename = "input.txt"):

    return "bar", "eXtension Cable"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day09Part1(filename)
    part2, desc2 = day09Part2(filename)
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

