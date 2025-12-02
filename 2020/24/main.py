import sys

def hash(x, y):
    return x*10**9+y
faceDown = set()
for line in sys.stdin:
    line = line.rstrip()
    x = line.count("n") - line.count("s")
    y = line.count("e") - line.count("w")
    h = hash(x,y)
    if h in faceDown:
        faceDown.remove(h)
    else:
        faceDown.add(h)
    print(len(faceDown))