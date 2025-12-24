def part_1(lines):
    is_beam = [False] * len(lines[0])
    s = next(filter(lambda x: x[1] == 'S', enumerate(lines[0])))[0]
    is_beam[s] = True
    splits = 0
    for line in lines:
        for i in range(len(line)):
            if line[i] == '^' and is_beam[i]:
                is_beam[i] = False
                if i < len(line) - 1:
                    is_beam[i + 1] = True
                if i > 0:
                    is_beam[i - 1] = True
                splits += 1
    return splits


def part_2(lines):
    beams = [0] * len(lines[0])
    s = next(filter(lambda x: x[1] == 'S', enumerate(lines[0])))[0]
    beams[s] = 1
    for line in lines:
        for i in range(len(line)):
            if line[i] == '^' and beams[i] > 0:
                if i < len(line) - 1:
                    beams[i + 1] += beams[i]
                if i > 0:
                    beams[i - 1] += beams[i]
                beams[i] = 0
    return sum(beams)


with open("inputs/day7.txt") as f:
    lines = list(map(lambda x: x.strip('\n'), f.readlines()))
    part_1_total = part_1(lines)
    part_2_total = part_2(lines)

print('part 1:', part_1_total)
print('part 2:', part_2_total)
