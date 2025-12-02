import sys
import numpy as np
import re

parser = re.compile(r"p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)")
class Robot:
    def __init__(self, x, y, vx, vy, boardWidth, boardHeight):
        self.position = np.array([x, y])
        self.velocity = np.array([vx, vy])
        self.board = np.array([boardWidth, boardHeight])
    
    def simulate(self, time):
        pos = self.position + time*self.velocity
        return pos%self.board

class Map:
    def __init__(self, sizeW, sizeH):
        self.robots: list[Robot] = []
        self.size = [sizeW, sizeH]

    def addRobot(self, x, y, vx, vy):
        self.robots.append(Robot(x, y, vx, vy, self.size[0], self.size[1]))
    
    def step(self, i):
        self.map = [[0]*self.size[0] for i in range(self.size[1])]
        for robot in self.robots:
            position = robot.simulate(i)
            self.map[position[1]][position[0]] += 1
        print("\n".join(["".join(["." if j == 0 else str(j) for j in i]) for i in self.map]))

#BW, BH = 11, 7
BW, BH = 101, 103


mapa = Map(BW, BH)

for line in sys.stdin:
    a, b, c, d = map(int,parser.match(line.strip()).groups())
    r = mapa.addRobot(a, b, c, d)

for i in range(1000):
    print(i)
    print()
    mapa.step(22+101*i)
    print()
    print()
    print()


