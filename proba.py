import numpy as np

def interpolate(points, values, x):
    return np.interp(x, points, values)

points =[1,2,3,4,5]
values =[2,3,5,7,11]
x =2.5

print(interpolate(points, values, x))

