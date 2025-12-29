import os
import itertools


class Node:
    def __init__(self, name):
        self.name = name
        self.outputs = set()
    def add_output(self, outputs):
        # add members of list to outputs set
        self.outputs.update(outputs)

def load_data(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)
    nodes = {}

    with open(data_file_path) as f:
        for line in f:
            nodename, namedoutputs = line.strip().split(":")
            node = Node(nodename)
            outputs = [ output.strip() for output in namedoutputs.split() ]
            node.add_output(outputs)
            nodes[nodename] = node

    return nodes

def dfs_count_paths(nodes, start = "you", end = "out"):
    # Count paths from start to end without storing full paths.
    # For each path we classify whether it passes through 'fft' and/or 'dac'.
    # Return a tuple: (none, only_fft, only_dac, both)
    memo = {}

    def dfs(current, visited, seen_fft, seen_dac):
        if current == end:
            if seen_fft and seen_dac:
                return (0, 0, 0, 1)
            if seen_fft:
                return (0, 1, 0, 0)
            if seen_dac:
                return (0, 0, 1, 0)
            return (1, 0, 0, 0)

        key = (current, seen_fft, seen_dac)
        if key in memo:
            return memo[key]

        total = [0, 0, 0, 0]
        for neighbor in nodes[current].outputs:
            if neighbor not in visited:  # avoid cycles
                next_seen_fft = seen_fft or (neighbor == "fft")
                next_seen_dac = seen_dac or (neighbor == "dac")
                visited.add(neighbor)
                counts = dfs(neighbor, visited, next_seen_fft, next_seen_dac)
                visited.remove(neighbor)
                for i in range(4):
                    total[i] += counts[i]

        memo[key] = tuple(total)
        return memo[key]

    start_seen_fft = (start == "fft")
    start_seen_dac = (start == "dac")
    visited = set([start])
    return dfs(start, visited, start_seen_fft, start_seen_dac)

def day11Part1(filename = "input.txt"):
    nodes = load_data(filename)
    counts = dfs_count_paths(nodes, start="you", end ="out")
    total_paths = sum(counts)
    return total_paths, "number of unique paths from 'you' to 'out'"

def day11Part2(filename = "input.txt"):
    nodes = load_data(filename)
    counts = dfs_count_paths(nodes, start="svr", end ="out")
    # index 3 is paths that contain both fft and dac
    return counts[3], "number of unique paths from 'svr' to 'out' containing 'fft' and 'dac'"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day11Part1(filename)
    # filename = "test2.txt"
    part2, desc2 = day11Part2(filename)
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

