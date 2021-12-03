from collections import Counter


with open('input.txt') as f:
    a = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

input_size = len(a)
n_size = len(a[0])


def part_one():
    frequency_list = ['0' if Counter(i)['0'] > input_size / 2 else '1' for i in zip(*a)]
    gamma = epsilon = '0b'

    for num in frequency_list:
        if num == '0':
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2) * int(epsilon, 2))


def part_two():
    global a

    b = a
    for i in range(n_size):
        most_frequent = '0' if Counter(tuple(zip(*b))[i])['0'] > len(b) / 2 else '1'
        b = [num for num in b if num[i] == most_frequent]
        if len(b) == 1:
            break
    oxygen = int(b[0], 2)

    b = a
    for i in range(n_size):
        most_frequent = '0' if Counter(tuple(zip(*b))[i])['0'] <= len(b) / 2 else '1'
        b = [num for num in b if num[i] == most_frequent]
        if len(b) == 1:
            break
    co2 = int(b[0], 2)

    print(oxygen * co2)


part_one()
part_two()
