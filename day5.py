def part_1(lines):
    fresh = 0
    ranges = []
    for line in lines:
        if '-' in line:
            range = line.split('-')
            ranges.append((int(range[0]), int(range[1])))
        elif line == '':
            continue
        else:
            id = int(line)
            for start, end in ranges:
                if start <= id and id <= end:
                    fresh += 1
                    break
    return fresh


def part_2(lines):
    ranges = []
    for line in lines:
        if '-' in line:
            range = line.split('-')
            ranges.append((int(range[0]), int(range[1])))

    ranges = sorted(ranges)
    cursor = 0
    count = 0
    print(ranges)
    for start, end in ranges:
        print("start", start, "end", end)
        print("cursor starts at", cursor)
        if cursor < start:
            count += end - start + 1
            cursor = end + 1
        elif cursor <= end:
            count += end - cursor + 1
            cursor = end + 1
        print("cursor ends at", cursor)
        print()
    return count


with open("inputs/day5.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    part_1_fresh_ingredients = part_1(lines)
    part_2_fresh_ingredients = part_2(lines)

print('part 1:', part_1_fresh_ingredients)
print('part 2:', part_2_fresh_ingredients)
