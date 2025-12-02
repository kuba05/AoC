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


def hashPosition(x, y, orientation):
    return (x * len(mapa) + y) * 4 + orientation


def doesEverExist(x, y, orientation):
    visited = set()
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
            x += dx
            y += dy
            hash = hashPosition(x, y, orientation)
            if hash in visited:
                # print("out")
                return False
            visited.add(hash)
    return True


def checkAllPossibleObstructionPositions(mapa, startingPosition):
    c = 0
    for j, line in enumerate(mapa):
        for i, char in enumerate(line):
            if char == ".":
                line[i] = "#"
                c += not doesEverExist(startingPosition[0], startingPosition[1], 0)
                line[i] = "."
        print("line", j)
    print(c)


checkAllPossibleObstructionPositions(mapa, position)
