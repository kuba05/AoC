import sys
import heapq


h = []

mapa = []

for i, line in enumerate(sys.stdin):
    line = line.strip()
    mapa.append(list(line))
    if "S" in line:
        start = (i, line.index("S"), 0)

costs = {}
moves = [
    [0,-1],
    [1, 0],
    [0, 1],
    [-1, 0],
]

def spread(pos):
    x, y, r = pos
    if mapa[x][y] == "E":
        return True
    dx, dy = moves[r]
    if mapa[x+dx][y+dy] != "#":
        newPos = (x+dx, y+dy, r)
        if costs.setdefault(newPos, 10**18) > costs[pos] + 1:
            heapq.heappush(h, (costs[pos]+1, newPos))
            costs[newPos] = costs[pos] + 1
    
    newPos = (x, y, (r+1)%4)
    if costs.setdefault(newPos,10**18) > costs[pos] + 1000:
        heapq.heappush(h, (costs[pos] + 1000, newPos))
        costs[newPos] = costs[pos] + 1000

    newPos = (x, y, (r-1)%4)
    if costs.setdefault(newPos, 10**18) > costs[pos] + 1000:
        heapq.heappush(h, (costs[pos] + 1000, newPos))
        costs[newPos] = costs[pos] + 1000
    return False

costs[start] = 0
spread(start)

while h:
    cost, pos = heapq.heappop(h)
    if cost != costs[pos]:
        continue
    if spread(pos):
        print(cost)
        break



    
