data = []
while True:
    line = input()
    if line == "":
        break
    data.append(line.split())

total = 0
print(data)
for i in range(len(data[0])):
    string = []
    for j in range(len(data) - 1):
        string.append(data[j][i])
    out = eval(data[-1][i].join(string))
    print(out)
    total += out
print(total)
