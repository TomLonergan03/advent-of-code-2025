part_1_joltage = 0
part_2_joltage = 0


def part_1(line):
    fst_idx = 0
    fst_val = 0
    for idx, char in enumerate(line[:-2]):
        if int(char) > fst_val:
            fst_val = int(char)
            fst_idx = idx
    snd_val = max(map(int, line[fst_idx + 1:-1]))
    return int(str(fst_val) + str(snd_val))


def part_2(line):
    joltage = ""
    for char in line:
        if len(joltage) < 12:
            joltage += char
        else:
            new_joltage = ""
            for i in range(len(joltage) - 1):
                if int(joltage[i]) < int(joltage[i + 1]):
                    new_joltage = joltage[:i] + joltage[i + 1:] + char
                    break
            if not new_joltage:
                new_joltage = joltage[:-1] + char
            if int(new_joltage) > int(joltage):
                joltage = new_joltage
    return int(joltage)


with open("inputs/day3.txt") as f:
    lines = f.readlines()
    for line in lines:
        part_1_joltage += part_1(line[:-1])
        part_2_joltage += part_2(line[:-1])

print('part 1:', part_1_joltage)
print('part 2:', part_2_joltage)
