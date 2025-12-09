ints = []
while True:
    line = input()
    if line == "":
        break
    a, b = map(int, line.split("-"))
    ints.append((a, b))

c = 0
while True:
    line = input()
    if line == "":
        break

nums = []
for i, ran in enumerate(ints):
    a, b = ran
    nums.append((a, -i - 1))
    nums.append((b, i + 1))

nums.sort()
open = set()
last = 0
for v, i in nums:
    if len(open) > 0:
        c += v - last
    if i < 0:
        if len(open) == 0:
            c += 1
        open.add(-i)
    else:
        open.remove(i)
    last = v


print(c)
