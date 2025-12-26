import os
import math

# def load_data(data_file_path):
#     # Get the directory of the current script
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     data_file_path = os.path.join(script_dir, data_file_path)
#     points = []

#     with open(data_file_path) as f:
#         operands = []
#         for line in f:
#             operands.append([ int(s) if s.isnumeric() else s for s in line.split()])

#     return operands

def load_data(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    with open(data_file_path) as f:
        operands = []
        for line in f:
            operands.append([ s for s in line.split()])

    return operands

def load_data2(data_file_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, data_file_path)

    with open(data_file_path) as f:
        operands = []
        for line in f:
            operands.append(line)

    return operands



def day06Part1(filename = "input.txt"):
    operands = load_data(filename)
    operands.append([ int(s) for s in operands[0]] )

    for row in operands[1:-2]:
        for idx, operand in enumerate(row):
            operand = int(operand)
            if operands[-2][idx] == '+':
                operands[-1][idx] += operand
            elif operands[-2][idx] == '*':
                operands[-1][idx] *= operand
            else:
                raise ValueError(f"unknown operator {operands[-2][idx]}")

    return sum(operands[-1]), "grand total"


def day06Part2(filename = "input.txt"):
    lines = load_data2(filename)
    maxlen = max( [ len(line) for line in lines ] )

    eq_result = [[0]]
    operands = [0]
    operator = ""
    n = 0
    for j in range(maxlen):
        divider_col = True
        for i, line in enumerate(lines[:-1]):
            if j >= len(line) or not line[j].isnumeric():
                continue
            operands[n] = operands[n] * 10 + int(line[j])
            divider_col = False
        n += 1
        if not divider_col:
            operands.append(0)
        if j < len(lines[-1]):
            operator = (operator + lines[-1][j]).strip()
        if divider_col:
            if operator == '+':
                eq_result[-1] = sum(operands[:-1])
            if operator == '*':
                eq_result[-1] = math.prod(operands[:-1])
            operands = [0]
            operator = ""
            eq_result.append(0)
            n = 0

    return sum(eq_result), "grand total"


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt"
    part1, desc1 = day06Part1(filename)
    part2, desc2 = day06Part2(filename)
    print(f"part 1    {part1} : {desc1}")
    print(f"part 2    {part2} : {desc2}")

