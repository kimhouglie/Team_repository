from math import sqrt

def distance(x1, y1, x2, y2):
    dx= x2- x1
    dy= y2- y1
    return sqrt(dx** 2+ dy** 2)

print(distance(1, 5, 5, 2))
print(round(distance(-2, 3, 1, 4), 4))
