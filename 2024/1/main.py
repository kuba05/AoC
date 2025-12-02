import sys

x = 0
L = []
R = []
for l in sys.stdin:
    a, b = map(int, l.split())
    L.append(a)
    R.append(b)

print(L, R)
for a in sorted(L):
    x += R.count(a) * a
print(x)
