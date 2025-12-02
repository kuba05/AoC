import sys

map = []
for i in sys.stdin:
    map.append(i.rstrip())

print(map)

newMap = [["."] * len(line) for line in map]


def findWord(x, y):
    out = 0
    # dirs = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    dirs = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    word = "MAS"
    for dir in dirs:
        for i in range(-1, 2):
            dX = x + i * dir[0]
            dY = y + i * dir[1]
            if (
                dX < 0
                or dX >= len(map)
                or dY < 0
                or dY >= len(map[0])
                or map[dX][dY] != word[i + 1]
            ):
                break
        else:
            for i in range(-1, 2):
                newMap[x + i * dir[0]][y + i * dir[1]] = word[i + 1]
            out += 1
    return out >= 2


count = 0
for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == "A":
            count += findWord(x, y)
            print(findWord(x, y))

print(count)
# print("\n".join("".join(line) for line in newMap))
