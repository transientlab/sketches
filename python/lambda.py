# lambda
import numpy as np


squirt = lambda u : np.sqrt(u)

def add_num(n):
    return lambda a : n + a

add_two = add_num(2)

def nothing():
    ...


print(nothing() or nothing())

# print(add_two(3))
# print(squirt(2))