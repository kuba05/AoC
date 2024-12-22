import sys

rulesA = {}

rulesB = {}
for line in sys.stdin:
    if line == "\n":
        break
    a, b = map(int, line.split("|"))
    rulesA.setdefault(a, set()).add(b)
    rulesB.setdefault(b, set()).add(a)


def isCorrect(numbers):
    forbidden = set()
    for n in numbers:
        if n in forbidden:
            break
        forbidden.update(rulesB.setdefault(n, set()))
    else:
        return True
    return False


sum = 0
for line in sys.stdin:
    out = []
    numbers = list(map(int, line.split(",")))
    if isCorrect(numbers):
        continue
    occurances = {i: 0 for i in numbers}
    for i in numbers:
        for x in rulesA.setdefault(i, set()):
            if x in occurances:
                occurances[x] += 1

    stack = list(filter(lambda i: occurances[i] == 0, occurances.keys()))

    while stack:
        cur = stack.pop()
        out.append(cur)
        for i in rulesA[cur]:
            if i not in occurances:
                continue
            occurances[i] -= 1
            if occurances[i] == 0:
                stack.append(i)
    sum += out[len(out) // 2]
    print(sum)
