line = input()
buffer = []

i = 0
blank = False
for x in line:
    for _ in range(int(x)):
        if blank:
            buffer.append(-1)
        else:
            buffer.append(i)
    blank = not blank
    if not blank:
        i += 1

i = 0
e = len(buffer) - 1
count = 0

while e >= i:
    if buffer[i] == -1:
        while buffer[e] == -1:
            e -= 1
        if e > i:
            count += i * buffer[e]
            e -= 1
    else:
        count += i * buffer[i]
    i += 1

print(count)
