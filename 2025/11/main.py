class Node:
    def __init__(self):
        self.edges = []

    def add_edge(self, other):
        self.edges.append(other)


nodes = {}
lines = open(0).readlines()[:-1]
nodes["out"] = Node()
for line in lines:
    line = line.strip()
    a, b = line.split(": ")
    nodes[a] = Node()

for line in lines:
    line = line.strip()
    a, b = line.split(": ")
    for node2 in b.split():
        nodes[a].add_edge(node2)


stack = [nodes["svr"]]
c = 0
while stack:
    print(len(stack))
    node = stack.pop()
    for edge in node.edges:
        if edge == "out":
            c += 1
            continue

        stack.append(nodes[edge])

print(c)

print(len(nodes))
