class Node:
    def getValue(self):
        raise NotImplementedError()


class ValueNode(Node):
    def __init__(self, value, key):
        self.value = value
        self.key = key

    def getValue(self):
        return self.value

    def getKids(self):
        return [self.key]


class OperationNode(Node):
    def __init__(self, entryA, entryB, key):
        self.entryA = entryA
        self.entryB = entryB
        self.value = None
        self.key = key

    def getValue(self):
        return self.computeValue()

    def getKids(self):
        return [*self.entryA.get().getKids(), *self.entryB.get().getKids(), self.key]


class AndNode(OperationNode):
    def computeValue(self):
        return self.entryA.getValue() and self.entryB.getValue()


class OrNode(OperationNode):
    def computeValue(self):
        return self.entryA.getValue() or self.entryB.getValue()


class XorNode(OperationNode):
    def computeValue(self):
        return self.entryA.getValue() != self.entryB.getValue()


class DelayedReference:
    def __init__(self, key, dict):
        self.key = key
        self.dict = dict

    def get(self):
        return self.dict[self.key]

    def getValue(self):
        return self.get().getValue()


import sys
import re

nodes = {}

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break

    a, b = line.split(": ")
    nodes[a] = ValueNode(bool(int(b)), a)

lines = [line for line in sys.stdin]

subMap = {}

for line in lines:
    line = line.strip()
    a, b = line.split(" -> ")
    o1, operation, o2 = a.split()
    match operation:
        case "AND":
            nodes[b] = AndNode(
                DelayedReference(o1, nodes), DelayedReference(o2, nodes), f"{a}->{b}"
            )
        case "OR":
            nodes[b] = OrNode(
                DelayedReference(o1, nodes), DelayedReference(o2, nodes), f"{a}->{b}"
            )
        case "XOR":
            nodes[b] = XorNode(
                DelayedReference(o1, nodes), DelayedReference(o2, nodes), f"{a}->{b}"
            )

if 0:
    n = sys.argv[1]
    print(nodes["s" + n].key)
    print(nodes["h" + n].key)
    print(nodes["z" + n].key)
    print(nodes["b" + n].key)
    print(nodes["c" + n].key)
    sys.exit()
for line in lines:
    # a = re.match(r"y(\d{2}) AND x\1 -> (.{3})", line)
    # b = re.match(r"y(\d{2}) XOR x\1 -> (.{3})", line)
    a = re.match(r"b(\d{2}) OR h\1 -> (.{3})", line)
    b = re.match(r"h(\d{2}) OR b\1 -> (.{3})", line)
    if a:
        subMap[a.group(2)] = "c" + a.group(1)

    if b:
        subMap[b.group(2)] = "c" + b.group(1)


for line in lines:
    a, b, c, d, e = line.strip().split(" ")
    if a in subMap:
        a = subMap[a]
    if c in subMap:
        c = subMap[c]
    if e in subMap:
        e = subMap[e]
    print(a, b, c, d, e)

print(subMap)
solution = []
print(",".join(sorted(solution)))
