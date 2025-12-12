import itertools


def solve(target, buttons):
    for on in range(1, len(buttons) + 1):
        for comb in itertools.combinations(buttons, on):
            me = [0] * len(target)
            for btn in comb:
                for field in btn:
                    me[field] = 1 - me[field]
            if me == target:
                print(on)
                return on
    raise ValueError()
    return 0


o = 0
for line in open(0).readlines()[:-1]:
    a = line.strip().split()
    target = a[0]
    _ = a[-1]
    buttons = a[1:-1]
    buttons = [(tuple(map(int, button[1:-1].split(",")))) for button in buttons]
    target = [1 if t == "#" else 0 for t in target[1:-1]]
    o += solve(target, buttons)
print(o)
