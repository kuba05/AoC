def is_invalid(i, per):
    x = str(i)
    l = len(x) // per
    if len(x) % per != 0:
        return False
    for j in range(per - 1):
        if x[l * j : l * (j + 1)] != x[l * (j + 1) : l * (j + 2)]:
            return False
    return True


max = 0


def solve(a, b, per):
    global max
    if b - a > max:
        max = b - a
    assert b > a
    c = 0
    while a <= b:
        if is_invalid(a, per):
            c += a
            break
        a += 1
    else:
        return 0
    assert len(str(a)) % per == 0
    # a is now the smallest invalid in the cycle
    step = 0
    for i in range(per):
        step += 10 ** (i * len(str(a)) // per)
    a += step
    while a <= b:
        while a <= b and is_invalid(a, per):
            #            print("counting", a, "step", step)
            c += a
            a += step
        if not is_invalid(a, per):
            step = 0
            for i in range(per):
                step += 10 ** (i * len(str(a)) // per)
            s = str(a)
            a = 0
            for i in range(per):
                print("x", per, len(str(a)))
                a += 10 ** ((i + 1) * (len(s) // per + 1) - 1)
            # print("New A", a, "step", step)

    #    print("for", per, "found", c)
    return c


def brute(a, b, per):
    c = 0
    for i in range(a, b + 1):
        for per in range(2, len(str(i)) + 1):
            if is_invalid(i, per):
                c += i
                break
    return c


def main(inpu):
    x = 0
    for i in inpu:
        a, b = i.split("-")
        x += solve(int(a), int(b), 2)
        x += solve(int(a), int(b), 3)
        x += solve(int(a), int(b), 5)
        x -= solve(int(a), int(b), 6)
        x += solve(int(a), int(b), 7)
    print(x)


def main_brute(inpu):
    x = 0
    for i in inpu:
        a, b = i.split("-")
        x += brute(int(a), int(b), 2)
    print(x)


def test():
    prev = 0
    per = 2
    last = 0
    for i in range(1000000):
        x = str(i)
        l = len(x) // per
        if len(x) % per != 0:
            continue
        for j in range(per - 1):
            if x[l * j : l * (j + 1)] != x[l * (j + 1) : l * (j + 2)]:
                break
        else:
            change = i - prev
            if last != change:
                print(prev, i)
                print("Now changning by", change)
                last = change
            prev = i


inpu = input().split(",")
# test()
main_brute(inpu)
main(inpu)
# print(max)
