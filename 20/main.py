import sys
import queue
from collections import defaultdict

mapa = set()
END = "E"
START = "S"
costs = defaultdict(lambda: 10**9)

for i, line in enumerate(sys.stdin):
    line = line.strip()
    for j, c in enumerate(line.strip()):
        if c == "#":
            continue
        mapa.add(i * 1 + j * 1j)
        if c == START:
            start_position = i * 1 + j * 1j
        if c == END:
            end_position = i * 1 + j * 1j


stack = queue.PriorityQueue()
stack.put((0, 0, end_position))
costs[end_position] = 0
counter = 0

while not stack.empty():
    cost, _, cur = stack.get()
    if cost != costs[cur]:
        continue
    move = 1
    for _ in range(4):
        move *= 1j
        new = cur + move
        if new not in mapa:
            continue
        if costs[new] > cost + 1:
            costs[new] = cost + 1
            stack.put((costs[new], counter, new))
            counter += 1

CHEAT_MOVES = [2, 1 + 1j, 2j, -1 + 1j, -2, -1 - 1j, -2j, 1 - 1j]
# find cheats
cheatCount = defaultdict(lambda: 0)
counts = 0
for pos in mapa:
    for move in CHEAT_MOVES:
        if pos + move in mapa:
            if costs[pos + move] + 2 < costs[pos]:
                cheatCount[costs[pos] - 2 - costs[pos + move]] += 1
                if costs[pos] - 2 - costs[pos + move] >= 100:
                    counts += 1


print(costs[start_position])
print(cheatCount)
print(counts)
