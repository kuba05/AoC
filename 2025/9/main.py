data = [tuple(map(int, line.strip().split(","))) for line in open(0).readlines()[:-1]]

size = 0

for a in data:
    for b in data:
        d = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if size < d:
            size = d

print(size)
