shapes = []

taken = []
for i in range(6):
    input()
    shapes.append([input(), input(), input()])
    taken.append(sum(x.count("#") for x in shapes[-1]))
    input()

t = 0


def solve(x, y, target):
    global t
    if x * y < sum(target[i] * taken[i] for i in range(6)):
        return 0
    if x // 3 * y // 3 >= sum(target):
        return 1
        # if x * y >= sum(target) * 9:
        # return 1
    t += 1
    print(
        x,
        y,
        target,
        "low",
        sum(target[i] * taken[i] for i in range(6)),
        "actual",
        x * y,
        "high",
        9 * sum(target),
    )
    return 1


c = 0
while line := input():
    size, target = line.split(": ")
    x, y = map(int, size.split("x"))
    target = list(map(int, target.split()))

    c += solve(x, y, target)
print(c)
print(t)
