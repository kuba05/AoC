from collections import defaultdict


lines = [list(line.strip()) for line in open(0).readlines()[:-1]]

for i, line in enumerate(lines):
    if "S" in line:
        j = line.index("S")
        break

c = 0
beans = {j: 1}
while True:
    new_beans = defaultdict(lambda: 0)
    i += 1
    if i == len(lines):
        break
    for bean in beans:
        count = beans[bean]
        if lines[i][bean] == ".":
            new_beans[bean] += count
        if lines[i][bean] == "^":
            new_beans[bean + 1] += count
            new_beans[bean - 1] += count

    beans = new_beans


print(sum(beans.values()))
