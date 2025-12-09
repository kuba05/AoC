data = [list(map(int, line.strip().split(","))) for line in open(0).readlines()[:-1]]


def distance(i, j):
    return (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2


dist = [
    (distance(pos1, pos2), (i, j), (pos1, pos2))
    for i, pos1 in enumerate(data)
    for j, pos2 in enumerate(data)
    if i > j
]
print(len(dist))

dist.sort(reverse=True)

union_find = [i for i in range(len(data))]


def join(x, y):
    if union_find[x] != x:
        join(union_find[x], y)
    else:
        union_find[x] = y


def find(x):
    if union_find[x] == x:
        return x
    par = find(union_find[x])
    union_find[x] = par
    return par


left = len(data) - 1
last = (None, None)
while left:
    _, (A, B), (dA, dB) = dist.pop()
    if find(A) == find(B):
        continue
    left -= 1
    last = (dA, dB)

    join(A, B)
print(last)
print("out", last[0][0] * last[1][0])
c = [0] * len(data)
for i, par in enumerate(union_find):
    c[find(i)] += 1
c.sort(reverse=True)
print(c)
print(c[0] * c[1] * c[2])
