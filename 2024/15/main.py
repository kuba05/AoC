import sys


mapa = []
position = ()
moves = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


for i, line in enumerate(sys.stdin):
    line = line.strip()
    if line == "":
        break
    mapa.append(list(line))
    if "@" in line:
        position = (i,list(line).index("@"))

def moveBlock(x, y, dx, dy):
    match mapa[x+dx][y+dy]:
        case "#":
            return False
        case ".":
            mapa[x+dx][y+dy] = mapa[x][y]
            mapa[x][y] = "."
            return True
        case "O":
            if moveBlock(x+dx, y+dy, dx, dy):
                mapa[x+dx][y+dy] = mapa[x][y]
                mapa[x][y] = "."
                return True
            else:
                return False


posX, posY = position
for move in list(input()):
    dx, dy = moves[move]
    if moveBlock(posX, posY, dx, dy):
        posX += dx
        posY += dy

sum = 0
for i, row in enumerate(mapa):
    for j, c in enumerate(row):
        if c == "O":
            sum += i*100+j
print(sum)
