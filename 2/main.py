import sys
import numpy as np

x = 0
for line in sys.stdin:
    levels = list(map(int, line.split()))
    # print(len(levels))
    for i in range(len(levels)):
        l = levels[:i] + levels[i + 1 :]
        dif = np.array([l[i + 1] - l[i] for i in range(len(l) - 1)])
        if (all(dif > 0) or all(dif < 0)) and max(abs(dif)) < 4:
            x += 1
            break
print(x)
