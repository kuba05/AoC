import sys
import re

commandList = {
    "mul": (r"(mul)\((\d{1,3}),(\d{1,3})\)", 3),
    "do": (r"(do\(\))", 1),
    "don't": (r"(don't\(\))", 1),
}


startIndexes = {}
prev = 0
for cmd in commandList:
    startIndexes[prev] = cmd
    prev += commandList[cmd][1]

commands = re.compile("|".join(commandList[cmd][0] for cmd in commandList))


def parseCommand(matchedGroups: list[str]):
    for i, group in enumerate(matchedGroups):
        if group != "":
            break

    command = startIndexes[i]
    args = commandList[command][1]
    return command, matchedGroups[i : args + i]


x = 0
on = True
for line in sys.stdin:
    for matched in commands.findall(line):
        cmd, args = parseCommand(matched)
        if cmd == "mul" and on:
            x += int(args[1]) * int(args[2])
        if cmd == "do":
            on = True
        if cmd == "don't":
            on = False

print(x)
