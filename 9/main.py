line = list(map(int, list(input())))
buffer = []
empty = {i: [] for i in range(10)}

i = 0
blank = False
position = 0
for x in line:
    if blank:
        empty.setdefault(x, []).append(position)
    else:
        i += 1
    position += x
    blank = not blank

for j in empty:
    empty[j] = [10**9] + list(reversed(empty[j]))
i -= 1

suma = 0
for x in reversed(line):
    blank = not blank
    if blank:
        position -= x
        continue

    leftMostPosition = position - x
    leftMostSize = -1
    for j in range(x, 10):
        if empty[j][-1] < leftMostPosition:
            leftMostPosition = empty[j][-1]
            leftMostSize = j
    if leftMostSize != -1:
        a = empty[leftMostSize].pop()
        if leftMostSize - x != 0:
            empty[leftMostSize - x].append(a + x)
            empty[leftMostSize - x].sort(reverse=True)
    print(f"group {i} is getting moved to position {leftMostPosition}")
    suma += i * (x * (leftMostPosition + leftMostPosition + x - 1) // 2)
    i -= 1
    position -= x

print(suma)
