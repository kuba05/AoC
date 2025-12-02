import sys
import math

mapa = []
positions = {}
for i, line in enumerate(sys.stdin):
    mapa.append(list(line.strip()))
    for j, c in enumerate(line.strip()):
        if c == ".":
            continue
        positions.setdefault(c, []).append((i,j))

print(positions)


count = 0
for char in positions:
    for i, pos1 in enumerate(positions[char]):
        for pos2 in positions[char][i+1:]:
            dir = [pos1[0]-pos2[0], pos1[1] - pos2[1]]
            k = math.gcd(dir[0], dir[1])
            dir = [dir[0]//k, dir[1]//k]

            i = 0
            while True:
                x, y = pos1[0] + i*dir[0], pos1[1] + i*dir[1]
                i += 1
                if not(0<=x<len(mapa) and 0<=y<len(mapa[x])):
                    break
                if mapa[x][y] == "#":
                    continue
                mapa[x][y] = "#"
                count += 1

            i = 0
            while True:
                x, y = pos1[0] + i*dir[0], pos1[1] + i*dir[1]
                i -= 1
                if not(0<=x<len(mapa) and 0<=y<len(mapa[x])):
                    break
                if mapa[x][y] == "#":
                    continue
                mapa[x][y] = "#"
                count += 1
                


print("\n".join("".join(line) for line in mapa))
print(count)
            

