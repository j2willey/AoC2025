import os
import math
import time

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

def get_all_sorted_distances_for_neighbor_pairs(points):
    # More pythonic: use itertools.combinations over indices to produce (i,j)
    import itertools
    distances = [ (i, j, math.dist(points[i], points[j]))
                  for i, j in itertools.combinations(range(len(points)), 2) ]
    distances.sort(key=lambda x: x[2])
    # print(f"computed {len(distances)} distances.")
    return distances


class UnionFindRank:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # path compression (recursive)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


CONNECTED_PAIRS = 1000
def day8Part1(filename = "input.txt"):
    global __day8Part1
    points = load_data(filename)

    distances = get_all_sorted_distances_for_neighbor_pairs(points)

    # Use Union-Find (rank) to build connected components from the closest pairs
    n = len(points)
    uf = UnionFindRank(n)
    for p1, p2, _ in distances[:CONNECTED_PAIRS]:
        uf.union(p1, p2)

    # collect root representatives and compute sizes
    from collections import Counter
    reps = [uf.find(i) for i in range(n)]
    sizes = sorted(Counter(reps).values(), reverse=True)
    # ensure we have at least 3 groups
    while len(sizes) < 3:
        sizes.append(0)
    product_of_top3 = sizes[0] * sizes[1] * sizes[2]

    print(f"product of top 3: {product_of_top3}")

    return product_of_top3, "product of 3 largest circuit sizes"

class UnionFindRankPart2:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sets = n
        print(f"UnionFindRankPart2 initialized with {n} sets.")
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return self.sets
        if ra < rb:
            self.parent[rb] = ra
        elif rb < ra:
            self.parent[ra] = rb
        self.sets -= 1
        return self.sets



def day8Part2(filename = "input.txt"):
    global __day8Part2
    points = load_data(filename)
    distances = get_all_sorted_distances_for_neighbor_pairs(points)

    # Use Union-Find (rank) to build connected components from the closest pairs
    n = len(points)
    uf = UnionFindRankPart2(n)
    xprod = 0
    for p1, p2, _ in distances:
        if  uf.union(p1, p2) <= 1:
            xprod = points[p1][0] * points[p2][0]
            break
    return xprod, "eXtension Cable"


if __name__ == "__main__":
    part1, desc1 = day8Part1()
    part2, desc2 = day8Part2()
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

