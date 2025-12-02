import sys
import functools


class Move:
    def __init__(self, dir: str, times: int):
        self.dir = dir
        self.times = times

    def vertical(count: int):
        if count < 0:
            return "^" * abs(count)
        return "v" * abs(count)

    def horizontal(count: int):
        if count < 0:
            return "<" * abs(count)
        return ">" * abs(count)


class DigitsSolver:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.i = 0
        self.position = [3, 2]

    def getPosition(self, char):
        match char:
            case "1":
                return [2, 0]
            case "2":
                return [2, 1]
            case "3":
                return [2, 2]
            case "4":
                return [1, 0]
            case "5":
                return [1, 1]
            case "6":
                return [1, 2]
            case "7":
                return [0, 0]
            case "8":
                return [0, 1]
            case "9":
                return [0, 2]
            case "0":
                return [3, 1]
            case "A":
                return [3, 2]

    def getOptions(self) -> list[str]:
        target = self.getPosition(self.sequence[self.i])
        now = self.position
        self.i += 1
        self.position = target
        # doesn't have 2 options

        if (now[0] == 3 and target[1] == 0) or (target[0] == 3 and now[1] == 0):
            return [
                Move.vertical(target[0] - now[0])
                + Move.horizontal(target[1] - now[1])
                + "A"
            ]

        return [
            Move.vertical(target[0] - now[0])
            + Move.horizontal(target[1] - now[1])
            + "A",
            Move.horizontal(target[1] - now[1])
            + Move.vertical(target[0] - now[0])
            + "A",
        ]


movesDecoder = {
    "<": {"<": ["A"], ">": ["<<A"], "^": ["v<A"], "v": ["<A"], "A": ["v<<A"]},
    ">": {">": ["A"], "<": [">>A"], "v": [">A"], "A": ["vA"], "^": ["v>A"]},
    "v": {"v": ["A"], "<": [">A"], ">": ["<A"], "^": ["vA"], "A": ["<vA"]},
    "^": {"^": ["A"], "<": [">^A"], ">": ["<^A"], "v": ["^A"], "A": ["<A"]},
    "A": {
        "^": [">A"],
        ">": ["^A"],
        "v": ["^>A"],
        "<": [">>^A"],
        "A": ["A"],
    },
}


class RobotSolver:
    def __init__(self, iterations=2):
        self.iterations = iterations

    def solve(self, text):
        for _ in range(self.iterations):
            prev = "A"
            out = ""
            for x in text:
                out += movesDecoder[x][prev]
                prev = x
            text = out
            print(_)
        return out

    def solveQuick(self, text):
        return self._solveQuick(text, self.iterations)

    @functools.cache
    def _solveQuick(self, text: str, iters: int) -> int:
        assert text[-1] == "A"
        if iters == 0:
            return len(text)
        x = 0
        prev = "A"
        for c in text:
            options = movesDecoder[c][prev]
            x += min([self._solveQuick(option, iters - 1) for option in options])

            prev = c
        return x


out = 0

for line in sys.stdin:
    line = line.strip()
    d = DigitsSolver(line)
    r = RobotSolver(25)
    l = 0
    for _ in range(4):
        options = d.getOptions()
        options = [r.solveQuick(option) for option in options]
        l += min(options)
    print(l)
    out += l * int(line[:-1])
print(out)
