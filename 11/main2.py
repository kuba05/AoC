line = list(map(int, input().split()))

cache = {}


def solve(element, iterationsLeft):
    if iterationsLeft == 0:
        return 1
    if (element, iterationsLeft) in cache:
        return cache[(element, iterationsLeft)]
    if element == 0:
        output = solve(1, iterationsLeft - 1)
    else:
        string = str(element)
        if len(string) % 2 == 0:
            output = solve(int(string[: len(string) // 2]), iterationsLeft - 1) + solve(
                int(string[len(string) // 2 :]), iterationsLeft - 1
            )
        else:
            output = solve(element * 2024, iterationsLeft - 1)
    cache[(element, iterationsLeft)] = output
    return output


count = 0
for x in line:
    count += solve(x, 75)
print(count)
