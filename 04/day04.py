import os

def load_data(data_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    banks = []
    with open(data_file_path) as f:
        room = []
        for line in f:
            room.append( [ c == '@' for c in line.strip() ])
    return room

def isPaperNeighbor(room, i, j):
    rows = len(room)
    cols = len(room[0])
    if i >= 0 and i < rows and j >= 0 and j < cols:
        return int(room[i][j])
    return 0

def isLiftable(room, i, j):
    # A paper can be lifted if it has no paper neighbors up, down, left, right
    return sum( [
        isPaperNeighbor(room, i-1, j-1),
        isPaperNeighbor(room, i-1, j),
        isPaperNeighbor(room, i-1, j+1),
        isPaperNeighbor(room, i, j-1),
        isPaperNeighbor(room, i, j+1),
        isPaperNeighbor(room, i+1, j-1),
        isPaperNeighbor(room, i+1, j),
        isPaperNeighbor(room, i+1, j+1) ])

def clear1pass(room):
    movables = 0
    clearedroom = [row[:] for row in room]

    moved = [ [" " for _ in range(len(room[0])) ] for _ in range(len(room)) ]
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j]:
                nieghbors = isLiftable(room, i, j)
                movables +=  int( nieghbors < 4)
                clearedroom[i][j] = False if nieghbors < 4 else True
                moved[i][j] = str(nieghbors)
            else:
                moved[i][j] = "."

    return movables, clearedroom

def day04Part1(filename = "input.txt"):
    room = load_data(filename)
    movables, room = clear1pass(room)
    return movables, "number of liftable paper rolls"

def day04Part2(filename = "input.txt"):
    room = load_data(filename)
    moved =1
    movables = 0
    while moved > 0:
        moved, room = clear1pass(room)
        movables += moved

    return movables, "number of liftable paper rolls"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day04Part1(filename)
    part2, desc2 = day04Part2(filename)
    print(f"part 1   {part1} : {desc1} ")
    print(f"part 2   {part2} : {desc2} ")
