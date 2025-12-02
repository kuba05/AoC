def do_rotate(old, by):
    out = (old + by) % 100
    if by < 0:
        by *= -1
        old = 100 - old

    count = 0
    if old != 100:
        count += 1
    by -= 100 - old
    return out, by // 100 + count


import sys

lines = sys.stdin.readlines()

trueIn = []
for line in lines:
    if line[0] == "L":
        trueIn.append(-int(line[1:]))
    else:
        trueIn.append(int(line[1:]))


count = 0
start = 50
for line in trueIn:
    start, c = do_rotate(start, line)
    if c > 1:
        print("moved by", line, "onto", start, "hit", c)
    count += c

print(count)
