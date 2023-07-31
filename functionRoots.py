import numpy as np

def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1



def newton(f, df, x0, epsilon):
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1

x0 = 1
epsilon = 0.0001
print(newton(f, df, x0, epsilon))
