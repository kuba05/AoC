import sys
import itertools

def add(a,b):
    return a + b
def mult(a,b):
    return a * b
i = 0
count = 0

def solve(values, remains):
    if len(values) == 0:
        return remains == 0
    if values[-1] > remains:
        return False
    if remains % values[-1] == 0:
        if solve(values[:-1], remains//values[-1]):
            return True
    lastOne = str(values[-1])
    if str(remains)[-len(lastOne):] == lastOne:
        if solve(values[:-1], int("0"+str(remains)[:-len(lastOne)])):
            return True
    return solve(values[:-1], remains-values[-1])

for line in sys.stdin:
    values = list(map(int, line.rstrip().replace(":", "").split()))
    target = values[0]
    numbers = values[1:]
    if solve(numbers, target):
        count += target


print(count)