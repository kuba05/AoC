import re
import numpy as np

number = re.compile(r"(\d+)")

c = 0
while True:
    A = np.array(list(map(int, number.findall(input()))))
    B = np.array(list(map(int, number.findall(input()))))
    price = list(map(int, number.findall(input())))
    input()

    for i in range(100):
        for j in range(100):
            if all(A*i + B*j - price == 0):
                c += i *3+j
                break

    print(c)