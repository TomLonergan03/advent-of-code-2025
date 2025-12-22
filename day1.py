dial = 50
land_zeros = 0
pass_zeros = 0


with open("inputs/day1.txt") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == 'L':
            change = int(line[1:])
            dial -= change
            pass_zeros += abs(dial) // 100
            if dial <= 0 and dial + change != 0:
                pass_zeros += 1
        else:
            dial += int(line[1:])
            pass_zeros += dial // 100
        dial %= 100
        if dial == 0:
            land_zeros += 1

print('part 1:', land_zeros)
print('part 2:', pass_zeros)
