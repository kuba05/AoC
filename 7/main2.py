import sys
import itertools

def add(a,b):
    return a + b
def mult(a,b):
    return a * b
def conc(a,b):
    return int(str(a)+str(b))
i = 0
count = 0
for line in sys.stdin:
    values = list(map(int, line.rstrip().replace(":", "").split()))
    target = values[0]
    initValue = values[1]
    c = values[2:]
    for operators in itertools.product([add, mult, conc], repeat=len(c)):
        current = initValue
        for value, oper in zip(c, operators):
            current = oper(current, value)
        if current == target:
            count += target
            break

print(count)