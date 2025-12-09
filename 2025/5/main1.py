ints = []
while True:
    line = input()
    if line == "":
        break
    a, b = map(int, line.split("-"))
    ints.append((a, b))

c = 0
while True:
    line = input()
    if line == "":
        break
    num = int(line)
    for a, b in ints:
        if a <= num <= b:
            c += 1
            break
print(c)
