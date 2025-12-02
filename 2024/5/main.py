import sys

rules = {}
for line in sys.stdin:
    if line == "\n":
        break
    a, b = map(int, line.split("|"))
    rules.setdefault(b, set()).add(a)

sum = 0
for line in sys.stdin:
    forbidden = set()
    numbers = list(map(int, line.split(",")))
    for n in numbers:
        if n in forbidden:
            break
        forbidden.update(rules.setdefault(n, set()))
    else:
        print("in")
        sum += numbers[len(numbers) // 2]
    print(sum)
