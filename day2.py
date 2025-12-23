from textwrap import fill

part_1_invalid_ids = 0
part_2_invalid_ids = 0


def part_1(id):
    id_str = str(id)
    id_len = len(id_str)
    if id_len % 2 != 0:
        return 0
    first_half = id_str[:id_len // 2]
    second_half = id_str[id_len // 2:]
    if first_half == second_half:
        return id
    return 0


def get_chunks(s, size):
    return [s[i:i + size] for i in range(0, len(s), size)]


def part_2(id):
    id_str = str(id)
    id_len = len(id_str)
    for size in range(1, id_len // 2 + 1):
        chunks = get_chunks(id_str, size)
        if len(set(chunks)) == 1:
            return id
    return 0


with open("inputs/day2.txt") as f:
    line = f.readline()
    ranges = line.split(',')
    for r in ranges:
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1]) + 1
        for id in range(start, end):
            part_1_invalid_ids += part_1(id)
            part_2_invalid_ids += part_2(id)

print('part 1:', part_1_invalid_ids)
print('part 2:', part_2_invalid_ids)
