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
    
#BW, BH = 11, 7
BW, BH = 101, 103


count = [[0,0], [0,0]]
for line in sys.stdin:
    a, b, c, d = map(int,parser.match(line.strip()).groups())
    r = Robot(a, b, c, d, BW, BH)
    pos = r.simulate(100)
    if pos[0] == BW//2 or pos[1] == BH//2:
        continue

    count[pos[0] < BW//2][pos[1] < BH//2] += 1
print(count)
print(count[0][0] * count[0][1] * count[1][0] * count[1][1])