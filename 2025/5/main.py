starts = {}
ends = {}
all_numbers = []
while True:
    line = input()
    if line == "":
        break

    a, b = map(int, line.split("-"))
    all_numbers += [a, b]
    if a in starts:
        starts[a] = max(starts[a], b)
    else:
        starts[a] = b
    if b in ends:
        ends[b] = max(ends[b], a)
    else:
        ends[b] = a

all_numbers.sort()


def find_number(x):
    s = 0
    e = len(all_numbers) - 1
    while (e - s) <= 1:
        if all_numbers[(s + e) // 2] < x:
            s = (s + e) // 2
        else:
            e = (s + e) // 2


...
