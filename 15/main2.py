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
    line = line.strip().replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
    if line == "":
        break
    mapa.append(list(line))
    if "@" in line:
        position = (i,list(line).index("@"))

def canMoveBlock(x, y, dx, dy, spread = True):
    match mapa[x+dx][y+dy]:
        case "#":
            return False
        case ".":
            return True
        case "[":
            if dx == 0:
                return canMoveBlock(x, y+dy, dx, dy)
            return canMoveBlock(x+dx, y, dx, dy) and canMoveBlock(x+dx, y+1, dx, dy, False)
        case "]":
            if dx == 0:
                return canMoveBlock(x, y+dy, dx, dy)
            return canMoveBlock(x+dx, y, dx, dy) and canMoveBlock(x+dx, y-1, dx, dy, False)
        
def moveBlock(x, y, dx, dy, spread=True):
    match mapa[x+dx][y+dy]:
        case "#":
            raise ValueError("Can't move walls!")
        case ".":
            ...
        case "[":
            moveBlock(x+dx, y+dy, dx, dy)
            if dx!= 0:
                moveBlock(x+dx, y+dy+1, dx, dy, False)
        case "]":
            moveBlock(x+dx, y+dy, dx, dy)
            if dx != 0:
                moveBlock(x+dx, y+dy-1, dx, dy, False)
        
    mapa[x+dx][y+dy] = mapa[x][y]
    mapa[x][y] = "."


posX, posY = position
for move in list(input()):
    dx, dy = moves[move]
    if canMoveBlock(posX, posY, dx, dy):
        moveBlock(posX,posY,dx,dy)
        posX += dx
        posY += dy

sum = 0
for i, row in enumerate(mapa):
    for j, c in enumerate(row):
        if c == "[":
            sum += i*100+j
print(sum)
