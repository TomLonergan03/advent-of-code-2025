from functools import reduce
import operator


def part_1(lines):
    total = 0
    cols = len(lines[0].split())
    sums = [[] for _ in range(cols)]
    for line in lines:
        for i, n in enumerate(line.split()):
            if n == '+':
                total += sum(sums[i])
            elif n == '*':
                total += reduce(operator.mul, sums[i], 1)
            else:
                sums[i].append(int(n))
    return total


def part_2(lines):
    total = 0
    ncols = len(lines[0].split())
    sums = [[] for _ in range(ncols)]
    for line in lines:
        for i, n in enumerate(line.split()):
            if n != '+' and n != '*':
                sums[i].append(n)
    widths = list(map(lambda x: max([len(y) for y in x]), sums))
    for width in widths:
        transpose = [[] for _ in range(width)]
        op = ''
        for i in range(len(lines)):
            for j in range(width):
                if lines[i][j].isdigit():
                    transpose[j].append(lines[i][j])
                elif lines[i][j] in ('*', '+'):
                    op = lines[i][j]
        values = []
        for row in transpose:
            values.append(int("".join(row)))
        if op == '+':
            total += sum(values)
        elif op == '*':
            total += reduce(operator.mul, values, 1)
        else:
            raise ValueError("Unknown op", op)
        lines = [line[width + 1:] for line in lines]
    return total


with open("inputs/day6.txt") as f:
    lines = list(map(lambda x: x.strip('\n'), f.readlines()))
    part_1_total = part_1(lines)
    part_2_total = part_2(lines)

print('part 1:', part_1_total)
print('part 2:', part_2_total)
