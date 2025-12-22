import os

def load_data(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    turns = []

    with open(data_file_path) as f:
        for line in f:
            letter = line[0]
            number = int(line[1:].strip())
            turns.append( (letter, number) )
    return turns

def day01Part1(filename = "input.txt"):
    global __day7Part1
    turns = load_data(filename)
    zero_count = 0
    location = 50
    for dir, steps in turns:
        if dir == 'L':
            location -= steps
        else:  # dir == 'R'
            location += steps
        location = (location % 100)
        if location == 0:
            zero_count += 1
    return zero_count, "zero crossings"

if __name__ == "__main__":
    # 48, 37
    part1, desc1 = day01Part1("input.txt")
    # part2, desc2 = day01Part2()
    print(f"part 1   {part1} : {desc1} ")
    # print(f"part 2  {desc2}:  {part2}")
