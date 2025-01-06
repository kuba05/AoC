import sys

patterns = list(input().split(", "))

trie = {}

for pattern in patterns:
    cur = trie
    for c in pattern:
        cur = cur.setdefault(c, {})
    cur["end"] = True

input()

c = 0
for target in sys.stdin:
    target = target.strip()
    
    canBeDone = [0] * (len(target) + 1)
    canBeDone[0] = 1
    for i, char in enumerate(target):
        if not canBeDone[i]:
            continue

        j = i
        cur = trie
        while j < len(target) and target[j] in cur:
            cur = cur[target[j]]
            j += 1
            if "end" in cur:
                canBeDone[j] += canBeDone[i]
    c += canBeDone[-1]

print(c)
    

