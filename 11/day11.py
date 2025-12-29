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


def day11Part1(filename = "input.txt"):
    # dfs traversal from start node "you" to end node "out"
    # return all unique paths
    nodes = load_data(filename)
    queue = [ ("you", ["you"]) ]
    unique_paths = set()
    while queue:
        current_node_name, path = queue.pop()
        current_node = nodes[current_node_name]
        for output in current_node.outputs:
            if output == "out":
                unique_path = path + [output]
                unique_paths.add( tuple(unique_path) )
            elif output not in path:
                new_path = path + [output]
                queue.append( (output, new_path) )

    return len(unique_paths), "number of unique paths from 'you' to 'out'"


def day11Part2(filename = "input.txt"):

    return "bar", "Part 2 result"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day11Part1(filename)
    part2, desc2 = day11Part2(filename)
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

