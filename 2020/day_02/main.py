import re


def part_one():
    with open('input.txt') as f:
        lines = f.readlines()

    p = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)\n?')
    v = 0
    for line in lines:
        match = p.match(line)
        if int(match.group(1)) <= int(match.group(4).count(match.group(3))) <= int(match.group(2)):
            v += 1

    print(v)


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()

    p = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)\n?')
    v = 0
    for line in lines:
        match = p.match(line)

        letter = match.group(3)
        password = match.group(4)

        index_1 = int(match.group(1))
        char_1 = password[index_1 - 1]
        index_2 = int(match.group(2))
        char_2 = password[index_2 - 1]

        if (char_1 == letter or char_2 == letter) and char_1 != char_2:
            v += 1

    print(v)


part_one()
part_two()
