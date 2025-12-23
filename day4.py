def part_1(lines):
    max_x = len(lines) - 1
    max_y = len(lines[0]) - 1
    accessible = 0
    final_grid = [list(line) for line in lines]
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            spaces = 0
            if lines[x][y] != '@':
                continue
            if x == 0 or lines[x - 1][y] != '@':
                spaces += 1
            if x == 0 or y == 0 or lines[x - 1][y - 1] != '@':
                spaces += 1
            if y == 0 or lines[x][y - 1] != '@':
                spaces += 1
            if x == 0 or y == max_y or lines[x - 1][y + 1] != '@':
                spaces += 1
            if y == max_y or lines[x][y + 1] != '@':
                spaces += 1
            if x == max_x or y == max_y or lines[x + 1][y + 1] != '@':
                spaces += 1
            if x == max_x or lines[x + 1][y] != '@':
                spaces += 1
            if x == max_x or y == 0 or lines[x + 1][y - 1] != '@':
                spaces += 1
            if spaces > 4:
                accessible += 1
                final_grid[x][y] = 'x'
                continue
    return accessible, final_grid


def part_2(grid):
    total_removed = 0
    while True:
        removed, new_grid = part_1(grid)
        if removed == 0:
            return total_removed
        total_removed += removed
        grid = new_grid


with open("inputs/day4.txt") as f:
    lines = list(map(lambda x: list(x.strip()), f.readlines()))
    part_1_accessible_rolls, _ = part_1(lines)
    part_2_removed_rolls = part_2(lines)

print('part 1:', part_1_accessible_rolls)
print('part 2:', part_2_removed_rolls)
