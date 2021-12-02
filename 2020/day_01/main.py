def part_one():
    with open('input.txt') as f:
        a = [int(line[:-1]) if line.endswith('\n') else int(line) for line in f.readlines()]

    for num_1 in a:
        r = 2020 - num_1
        if r in a:
            print(f'{num_1} * {r} = {num_1 * r}')
            break


def part_two():
    with open('input.txt') as f:
        a = [int(line[:-1]) if line.endswith('\n') else int(line) for line in f.readlines()]

    for num_1 in a:
        b = a
        b.remove(num_1)
        for num_2 in b:
            r = 2020 - num_1 - num_2
            if r in a:
                print(f'{num_1} * {num_2} * {r} = {num_1 * num_2 * r}')
                break


part_one()
part_two()
