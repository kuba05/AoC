import sys

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
            A = [2*pos1[0]-pos2[0], 2*pos1[1] - pos2[1]]
            B = [2*pos2[0]-pos1[0], 2*pos2[1] - pos1[1]]
            print(pos1,pos2)
            print(A,B)
            for x,y in [A,B]:
                if not(0<=x<len(mapa) and 0<=y<len(mapa[x])):
                    continue
                if mapa[x][y] == "#":
                    continue
                mapa[x][y] = "#"
                count += 1


print("\n".join("".join(line) for line in mapa))
print(count)
            

