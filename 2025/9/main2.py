data = [tuple(map(int, line.strip().split(","))) for line in open(0).readlines()[:-1]]

by_x = sorted(
    [
        [a for a in data if a[0] == target_x]
        for target_x in set(line[0] for line in data)
    ],
    key=lambda a: a[0][0],
)
by_y = sorted(
    [
        [a for a in data if a[1] == target_y]
        for target_y in set(line[1] for line in data)
    ],
    key=lambda a: a[0][1],
)

assert all(len(a) == 2 for a in by_x)
assert all(len(a) == 2 for a in by_y)

print(len(data), max(x[0] for x in data), max(x[1] for x in data))

size = 0


def sgn(a):
    if a == 0:
        return 0
    if a < 0:
        return -1
    return 1


def admitable(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return True
    y0, y1 = sorted((a[1], b[1]))
    x0, x1 = sorted((a[0], b[0]))

    for c in by_x:
        p0 = c[0]
        p1 = c[1]
        px = p0[0]
        py0, py1 = sorted((p0[1], p1[1]))
        if not (x0 < px < x1):
            continue

        if py0 <= y0 < py1:
            return False

        if py0 < y1 <= py1:
            return False

    for c in by_y:
        p0 = c[0]
        p1 = c[1]
        py = p0[1]
        px0, px1 = sorted((p0[0], p1[0]))
        if not (y0 < py < y1):
            continue

        if px0 <= x0 < px1:
            return False

        if px0 < x1 <= px1:
            return False

    return True


for a in data:
    for b in data:
        if admitable(a, b):
            d = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if size < d:
                size = d

print(size)
