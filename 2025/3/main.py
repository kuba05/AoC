def solve(data, remains):
    if remains == 0:
        return 0
    if remains == 1:
        return max(data)
    first = max(data[: -remains + 1])

    second = solve(data[data.index(first) + 1 :], remains - 1)
    return first * 10 ** (remains - 1) + second


def main():
    x = 0
    while True:
        line = input()
        if line == "":
            break
        data = list(map(int, list(line)))
        a = solve(data, 12)
        x += a
        print(a, x)


main()
