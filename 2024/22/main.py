def step(number: int):
    def prune(a):
        return a % 16777216

    def mix(a, b):
        return a ^ b

    number = prune(mix(number, number * 64))
    number = prune(mix(number // 32, number))
    number = prune(mix(number, number * 2048))
    return number


import sys

s = 0
for i in sys.stdin:
    line = i.strip()
    number = int(line)
    for _ in range(2000):
        number = step(number)
    s += number
print(s)
