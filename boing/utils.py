import math

def normalised(x, y):
    length = math.hypot(x, y)
    return x / length, y / length


def sign(x):
    return -1 if x < 0 else 1