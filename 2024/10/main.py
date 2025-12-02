import sys

mapa = []
pos = {i: set() for i in range(10)}

for i,line in enumerate(sys.stdin):
    if line.strip() == "":
        break
    mapa.append(list(map(int,line.strip())))
    for j, c in enumerate(mapa[-1]):
        pos[c].add((i,j))

moves = [(1,0),(0,1),(-1,0),(0,-1)]
def solve(number, x, y):

    c = set() 
    if number == 10:
        return {(x,y)}
    for dx, dy in moves:
        if (x+dx, y+dy) in pos[number]:
            c = c |solve(number+1, x+dx, y+dy)
    return c

c = 0
for i in pos[0]:
    c += len(solve(1,i[0], i[1]))
print(c)


