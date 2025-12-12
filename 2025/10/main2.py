from numpy import array
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def solveEquationOverInt(A, b):
    """Finds x s.t. A x = b and x is in R^n"""
    constraints = LinearConstraint(A, b, b)
    integrality = np.ones(A.shape[1])
    bounds = Bounds(lb=0, ub=np.inf)
    c = np.ones(A.shape[1])
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    if res.success:
        solution = np.round(res.x).astype(int)
    else:
        raise ValueError()
    assert all(A @ solution == b)
    return solution


def solve(target, buttons):
    matrix = array(
        [[1 if i in button else 0 for i in range(len(target))] for button in buttons],
        dtype=int,
    ).T

    target = array(target, dtype=int)
    print(matrix.shape, target.shape)
    x = solveEquationOverInt(matrix, target)
    print(sum(x))
    return sum(x)

    print(nullspace)
    print(x)
    assert all(matrix.dot(x) == target)
    return 0


o = 0
for line in open(0).readlines()[:-1]:
    a = line.strip().split()
    _ = a[0]
    target = tuple(map(int, a[-1][1:-1].split(",")))
    buttons = a[1:-1]
    buttons = [(tuple(map(int, button[1:-1].split(",")))) for button in buttons]
    o += solve(target, buttons)
print(o)
