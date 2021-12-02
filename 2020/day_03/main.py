with open('input.txt') as f:
    # Triple list comprehension LOL
    slope = [list(col) for col in zip(*[[char for char in line if char != '\n'] for line in f.readlines()])]


def part_one(delta_x, delta_y):
    bottom = len(slope[0])
    x, y = 0, 0

    trees = 0
    while x < bottom - 1:
        y = (y + delta_y) % len(slope)
        x += delta_x
        if slope[y][x] == '#':
            trees += 1

    return trees


print(part_one(1, 3))
print(part_one(1, 1) * part_one(1, 3) * part_one(1, 5) * part_one(1, 7) * part_one(2, 1))
