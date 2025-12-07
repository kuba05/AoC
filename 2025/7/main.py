lines = [list(line.strip()) for line in open(0).readlines()[:-1]]

for i, line in enumerate(lines):
    if "S" in line:
        j = line.index("S")
        break

c = 0
beans = [j]
while True:
    new_beans = set()
    i += 1
    if i == len(lines):
        break
    for bean in beans:
        if lines[i][bean] == ".":
            new_beans.add(bean)
        if lines[i][bean] == "^":
            c += 1
            new_beans.add(bean - 1)
            new_beans.add(bean + 1)

    beans = new_beans


print(c)
