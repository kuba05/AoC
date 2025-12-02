import sys
import queue
from collections import defaultdict

occupied = set()

for i, line in enumerate(sys.stdin):
    if i == 1024:
        break
    a, b = map(int,line.split(","))
    occupied.add(a+b*1j)

position = 0 
end = (1+1j)*70

costs = defaultdict(lambda: 2**18)

costs[position] = 0

q = queue.PriorityQueue()
q.put((0, 0, position))

i = 0

while not q.empty():
    cost, _, cur = q.get()
    if cost != costs[cur]:
        continue
    m = 1
    for _ in range(4):
        m *= 1j
        if not (0 <= (cur+m).real <= end.real and 0 <= (cur+m).imag <= end.imag):
            continue
        if cur+m in occupied:
            continue

        if costs[cur+m] > costs[cur] + 1:
            i += 1
            costs[cur+m] = costs[cur] + 1
            q.put((costs[cur+m], i, cur+m))

print(costs[end])