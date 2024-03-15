import numpy as np


def power(a, n):
    return np.linalg.matrix_power(a, n)

def eigenvalue(a):
    return np.linalg.eigvals(a)

def det(a):
    return np.linalg.det(a)

def solve(a, b):
    return np.linalg.solve(a, b)

def dotpro(a, b):
    return np.linalg.dot(a, b)

def innerpro(a, b):
    return np.linalg.inner(a, b)

def complexangle(z):
    return np.angle(z)
