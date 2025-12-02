import sys

blocksByRows = {}
mapa = []

position = []
orientation = 0
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for j, line in enumerate(sys.stdin):
    line = line.strip()
    for i, char in enumerate(line):
        if char == "^":
            position = [j, i]
            continue

    mapa.append(list(line))

x, y = position
mapa[x][y] = "X"
while True:
    #  print()
    #  print("\n".join("".join(row) for row in mapa))
    dx, dy = direction[orientation]
    if x + dx < 0 or y + dy < 0 or x + dx >= len(mapa) or y + dy >= len(mapa[0]):
        break
    # print(mapa[x + dx][y + dy])
    if mapa[x + dx][y + dy] == "#":
        orientation = (orientation + 1) % 4
    else:
        mapa[x + dx][y + dy] = "X"
        x += dx
        y += dy

c = 0
for line in mapa:
    for i in line:
        c += i == "X"
print(c)
