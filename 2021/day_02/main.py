import re


with open('input.txt') as f:
    lines = f.readlines()
p = re.compile(r'([a-z]+) (\d)\n?')
x1 = y1 = x2 = y2 = aim = 0

for line in lines:
    match = p.match(line)

    cmd = match.group(1)
    n = int(match.group(2))

    if cmd == 'forward':
        x1 += n
        x2 += n
        y2 += n * aim
    elif cmd == 'down':
        y1 += n
        aim += n
    else:
        y1 -= n
        aim -= n


print(x1 * y1)
print(x2 * y2)
