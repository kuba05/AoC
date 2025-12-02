def step(number: int):
    def prune(a):
        return a % (2**24)

    def mix(a, b):
        return a ^ b

    number = prune(mix(number, number << 6))
    number = prune(mix(number >> 5, number))
    number = prune(mix(number, number << 11))
    return number


import sys
from collections import defaultdict

prices = []
s = 0
for i in sys.stdin:
    line = i.strip()
    number = int(line)
    prices.append([number % 10])
    for _ in range(2000):
        number = step(number)
        prices[-1].append(number % 10)
diffs = [[j - i for i, j in zip(price[:-1], price[1:])] for price in prices]

x = 0


db = defaultdict(lambda: 0)

for diff, cost in zip(diffs, prices):
    temp = {}
    for A, B, C, D, c in zip(diff[:-3], diff[1:-2], diff[2:-1], diff[3:], cost[4:]):
        if (A, B, C, D) not in temp:
            temp[(A, B, C, D)] = c
    for key, value in temp.items():
        db[key] += value


print(max(db.values()))
