import re
import numpy as np

number = re.compile(r"(\d+)")

def det(matrix):
    return matrix[0,0] * matrix[1,1] - matrix[1,0] * matrix[0,1]
c = 0
while True:
    A = np.array(list(map(int, number.findall(input()))), dtype=int)
    B = np.array(list(map(int, number.findall(input()))),dtype = int)
    C = np.array(list(map(int, number.findall(input()))),dtype = int) + 10000000000000
    input()

    u = det(np.array([A, B], dtype=int))
    v = det(np.array([A, C]))
    w = det(np.array([C, B]))
    if v%u == 0 and w%u == 0:
        c += w//u * 3 +v//u
    print(c)
    