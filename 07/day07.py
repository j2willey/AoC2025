import os

def load_data(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, 'input.txt')

    rows = []

    with open(data_file_path) as f:
        for line in f:
            rows.append(line.strip())
    return rows

def day7Part1(filename = "input.txt"):
    global __day7Part1
    rows = load_data("input.txt")
    count = 0
    for i, row in enumerate(rows):
        if i == 0:
            continue
        # Loop over all instances of 'S' in the previous (above) row; iterate their indices
        newrow = list(row)
        for j in [idx for idx, ch in enumerate(rows[i-1]) if ch == 'S']:
            c = row[j]
            if  c == '^':
                newrow[j-1] = 'S'
                newrow[j+1] = 'S'
                count += 1
            else:
                newrow[j] = 'S'
        rows[i] = ''.join(newrow)
    #for row in rows:
    #    print(row)
    return count, "splits"

def day7Part2(filename = "input.txt"):
    global __day7Part1
    rows = load_data("input.txt")
    for i, row in enumerate(rows):
        if i == 0:
            rows[0] = [1 if char == 'S' else 0 for char in row]
            continue
        newrow = [0] * len(row)
        for j, c in enumerate(row):
            if  c == '^':
                newrow[j-1] += rows[i-1][j]
                newrow[j+1] += rows[i-1][j]
            else:
                newrow[j] += rows[i-1][j]
        rows[i] = newrow
    # for row in rows:
    #     print(" ".join([str(i) for i in row]))
    return sum(rows[-1]), "paths"


if __name__ == "__main__":
    part1, desc1 = day7Part1()
    part2, desc2 = day7Part2()
    print(f"part 1  {desc1}:  {part1}")
    print(f"part 2  {desc2}:  {part2}")

