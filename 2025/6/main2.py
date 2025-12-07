lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

line = lines[-1]
last = -1
indexes = []
while len(line):
    dx = len(line) - len(line.lstrip()) + 1
    indexes.append(last + dx)
    last += dx
    line = line.lstrip()[1:]
indexes[-1] += 1

parts = []
lastindex = 0
for index in indexes[1:]:
    parts.append([])
    for i, line in enumerate(lines):
        parts[-1].append(line[lastindex:index])
    lastindex = index
total = 0
for part in parts:
    numbers = []
    for position in range(len(part[0])):
        numbers.append("".join([word[position] for word in part[:-1]]).strip())
        if numbers[-1] == "":
            numbers.pop()
    op = part[-1].strip()
    out = eval(op.join(numbers))
    print(out)
    total += out

print(total)
