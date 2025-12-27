import os
import itertools
from collections import deque

def load_data(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)
    points = []

    with open(data_file_path) as f:
        machines = []
        for line in f:
            ltdiag = ""
            buttons = []
            joltage = []
            for part in line.split(' '):
                if part[0] == "[":
                    ltdiag = part.strip("[]")
                    ltbyte = 0
                    for i, ch in enumerate(ltdiag):
                        if ch == '#':
                            ltbyte |= (1 << int(i))
                elif part[0] == "(":
                    button = 0
                    for bit in part.strip("()").split(','):
                        button |= (1 << int(bit))
                    buttons.append(button)
                elif part[0] == "{":
                    joltage = part.strip().strip("{}").split(',')
                else:
                    raise ValueError(f"Unknown data format {part}")
            machines.append( (ltdiag, ltbyte, buttons, joltage) )
    return machines


def day10Part1(filename = "input.txt"):
    machines = load_data(filename)
    # For each machine, find minimal button presses to reach ltbyte from 0.
    def min_presses_bfs(target, buttons, nbits):
        # BFS over light states (0..(1<<nbits)-1), edges toggle by button masks.
        if target == 0:
            return 0
        if not buttons:
            return None
        q = deque()
        q.append((0, 0))
        seen = {0}
        while q:
            state, dist = q.popleft()
            for b in buttons:
                nxt = state ^ b
                if nxt == target:
                    return dist + 1
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, dist + 1))
        return None

    totals = []
    for idx, (ltdiag, ltbyte, buttons, joltage) in enumerate(machines, start=1):
        nbits = len(ltdiag)
        best = min_presses_bfs(ltbyte, buttons, nbits)
        totals.append(best)
        # print(f"Machine {idx}: target=0b{ltbyte:0{nbits}b}, buttons={len(buttons)}, min_presses={best}")

    # Sum of found minimal presses (ignore unreachable machines)
    total_presses = sum(x for x in totals if x is not None)
    return total_presses, "total minimal presses"


def day10Part2(filename = "input.txt"):

    return "bar", "Part 2 result"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day10Part1(filename)
    part2, desc2 = day10Part2(filename)
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

