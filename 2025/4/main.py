class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.edges = []
        self.removed = False

    def add_edge(self, other):
        self.edges.append(other)

    def to_remove(self):
        return (not self.removed) and len(self.edges) <= 3

    def remove(self):
        self.removed = True
        for edge in self.edges:
            edge.edges.remove(self)
        return self.edges


mapa = {}
i = 0
while True:
    line = input()
    if line == "":
        break
    for j, c in enumerate(line):
        if c == "@":
            mapa[i + 1j * j] = 1
    i += 1

pos = [k for k in mapa.keys()]

x = 0

while pos:
    i = pos.pop()
    if i not in mapa:
        continue
    c = 0
    to_add = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            move = dx + 1j * dy
            if move == 0:
                continue
            if move + i in mapa:
                c += 1
                to_add.append(move + i)
    if c < 4:
        x += 1
        del mapa[i]
        pos += to_add

print(x)
