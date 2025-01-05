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
    
    canBeDone = [False] * (len(target) + 1)
    canBeDone[0] = True
    for i, char in enumerate(target):
        if not canBeDone[i]:
            continue

        cur = trie
        while i < len(target) and target[i] in cur:
            cur = cur[target[i]]
            i += 1
            if "end" in cur:
                canBeDone[i] = True
    if canBeDone[-1]:
        c += 1
        print("YES")
    else:
        print("NO")

print(c)
    

