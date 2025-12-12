import functools


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


@functools.cache
def paths(start, end):
    if start == end:
        return 1
    return sum(paths(edge, end) for edge in nodes[start].edges)


o = paths("svr", "dac") * paths("dac", "fft") * paths("fft", "out")
o += paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out")
print(o)
