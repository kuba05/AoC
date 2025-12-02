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
good_parents = {}

moves = [
    [0,-1],
    [1, 0],
    [0, 1],
    [-1, 0],
]

def spread(pos, h, costs):
    x, y, r = pos
    if mapa[x][y] == "E":
        return True
    dx, dy = moves[r]
    if mapa[x+dx][y+dy] != "#":
        newPos = (x+dx, y+dy, r)
        if costs.setdefault(newPos, 10**18) >= costs[pos] + 1:
            good_parents.setdefault(newPos, []).append(pos)
        if costs.setdefault(newPos, 10**18) > costs[pos] + 1:
            heapq.heappush(h, (costs[pos]+1, newPos))
            costs[newPos] = costs[pos] + 1
    
    newPos = (x, y, (r+1)%4)
    if costs.setdefault(newPos, 10**18) >= costs[pos] + 1000:
        good_parents.setdefault(newPos, []).append(pos)
    if costs.setdefault(newPos,10**18) > costs[pos] + 1000:
        heapq.heappush(h, (costs[pos] + 1000, newPos))
        costs[newPos] = costs[pos] + 1000

    newPos = (x, y, (r-1)%4)
    if costs.setdefault(newPos, 10**18) >= costs[pos] + 1000:
        good_parents.setdefault(newPos, []).append(pos)
    if costs.setdefault(newPos, 10**18) > costs[pos] + 1000:
        heapq.heappush(h, (costs[pos] + 1000, newPos))
        costs[newPos] = costs[pos] + 1000
    return False

def spreadBackwards(pos, h, costs):
    x, y, r = pos
    if pos == start:
        return True
    dx, dy = moves[(r+2)%4]
    if mapa[x+dx][y+dy] != "#":
        newPos = (x+dx, y+dy, r)
        if costs.setdefault(newPos, 10**18) >= costs[pos] + 1:
            good_parents.setdefault(newPos, []).append(pos)
        if costs.setdefault(newPos, 10**18) > costs[pos] + 1:
            heapq.heappush(h, (costs[pos]+1, newPos))
            costs[newPos] = costs[pos] + 1
    
    newPos = (x, y, (r+1)%4)
    if costs.setdefault(newPos, 10**18) >= costs[pos] + 1000:
        good_parents.setdefault(newPos, []).append(pos)
    if costs.setdefault(newPos,10**18) > costs[pos] + 1000:
        heapq.heappush(h, (costs[pos] + 1000, newPos))
        costs[newPos] = costs[pos] + 1000

    newPos = (x, y, (r-1)%4)
    if costs.setdefault(newPos, 10**18) >= costs[pos] + 1000:
        good_parents.setdefault(newPos, []).append(pos)
    if costs.setdefault(newPos, 10**18) > costs[pos] + 1000:
        heapq.heappush(h, (costs[pos] + 1000, newPos))
        costs[newPos] = costs[pos] + 1000
    return False

finish = None

costs[start] = 0
spread(start, h, costs)
while h:
    cost, pos = heapq.heappop(h)
    if cost != costs[pos]:
        continue
    if spread(pos, h, costs):
        finish = pos
        print(cost)
        break



costsBackwards = {finish: 0}
spreadBackwards(finish, h, costsBackwards)

while h:
    cost, pos = heapq.heappop(h)
    if cost != costsBackwards[pos]:
        continue
    if spreadBackwards(pos, h, costsBackwards):
        print(cost)
        break

out = set()

for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        for k in range(4):
            if costsBackwards.setdefault((i,j,k),0) + costs.setdefault((i,j,k),0) == costsBackwards[start]:
                out.add((i,j))

for i,j in out:
    mapa[i][j] = "O"

print(len(out))
    
