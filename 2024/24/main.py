class Node:
    def getValue(self):
        raise NotImplementedError()


class ValueNode(Node):
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value


class OperationNode(Node):
    def __init__(self, entryA, entryB):
        self.entryA = entryA
        self.entryB = entryB
        self.value = None

    def getValue(self):
        if self.value is None:
            self.value = self.computeValue()
        return self.value


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

    def getValue(self):
        return self.dict[self.key].getValue()


import sys

nodes = {}

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break

    a, b = line.split(": ")
    nodes[a] = ValueNode(bool(int(b)))

for line in sys.stdin:
    line = line.strip()
    a, b = line.split(" -> ")
    o1, operation, o2 = a.split()
    match operation:
        case "AND":
            nodes[b] = AndNode(DelayedReference(o1, nodes), DelayedReference(o2, nodes))
        case "OR":
            nodes[b] = OrNode(DelayedReference(o1, nodes), DelayedReference(o2, nodes))
        case "XOR":
            nodes[b] = XorNode(DelayedReference(o1, nodes), DelayedReference(o2, nodes))

countA = 0
for node in sorted((n for n in nodes.keys() if n[0] == "x"), reverse=True):
    countA <<= 1
    countA += nodes[node].getValue()
print(countA)
countB = 0
for node in sorted((n for n in nodes.keys() if n[0] == "y"), reverse=True):
    countB <<= 1
    countB += nodes[node].getValue()
print(countB)
count = 0
for node in sorted((n for n in nodes.keys() if n[0] == "z"), reverse=True):
    count <<= 1
    count += nodes[node].getValue()
print(count)
print(countA + countB == count)
