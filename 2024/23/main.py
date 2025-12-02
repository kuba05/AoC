import networkx as nx
import sys
from collections import defaultdict

edgelist = []
edgesByNode = defaultdict(lambda: [])

nodes = set()

for line in sys.stdin:
    a, b = line.strip().split("-")
    edgelist.append((a, b))
    nodes.add(a)
    nodes.add(b)
    edgesByNode[a].append(b)
    edgesByNode[b].append(a)


graph = nx.from_edgelist(edgelist)

nx.find_cliques(graph)

found = set()
for node in nodes:
    for second in edgesByNode[node]:
        if node > second:
            continue
        for last in edgesByNode[second]:
            if second > last:
                continue
            if last in edgesByNode[node]:
                found.add((node, second, last))
print(len(found))

found = {i for i in found if any("t" == j[0] for j in i)}
print(len(found))
