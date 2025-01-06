import sys

mapa = []


chars = {}

for i, line in enumerate(sys.stdin):
    line = line.strip()
    mapa.append(list(line))
    for j, c in enumerate(line):
        chars.setdefault(c, []).append((i, j))

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def inBounds(x, y):
    return 0 <= x < len(mapa) and 0 <= y < len(mapa[x])


def spreadAll(char, positions):
    done = set()
    c = 0
    for pos in positions:
        a, b = spread(char, pos, done)
        print(char, b, a)
        c += a * b
    return c


def spread(c, pos, done):
    if pos in done:
        return 0, 0
    boundary = 0
    area = 1
    x, y = pos
    done.add((x, y))
    for dx, dy in moves:
        if (x + dx, y + dy) not in done:
            if inBounds(x + dx, y + dy) and mapa[x + dx][y + dy] == c:
                a, b = spread(c, (x + dx, y + dy), done)
                boundary += a
                area += b
            else:
                boundary += 1
    return boundary, area


s = 0
for char in chars:
    a = spreadAll(char, chars[char])
    s += a
print(s)
