import sys


def load():
    lock = [list(input()) for _ in range(7)]

    pins = [0] * 5
    for i in range(5):
        for j in range(7):
            if lock[j][i] != lock[0][i]:
                break
        pins[i] = j

    return lock[0][0] == "#", pins


keys = []
locks = []

while True:
    lock, pins = load()
    if lock:
        locks.append(pins)
    else:
        keys.append(pins)

    if input() != "":
        break

c = 0
for key in keys:
    for lock in locks:
        if all(key[i] >= lock[i] for i in range(5)):
            c += 1
print(c)
