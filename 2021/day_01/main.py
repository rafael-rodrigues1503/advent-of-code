with open('input.txt') as f:
    a = [int(line[:-1]) if line.endswith('\n') else int(line) for line in f.readlines()]


def part_one():
    num = 0
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            num += 1
    print(num)


def part_two():
    num = 0
    for i in range(2, len(a) - 1):
        if a[i - 1] + a[i] + a[i + 1] > a[i - 2] + a[i - 1] + a[i]:
            num += 1
    print(num)


part_one()
part_two()
