import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    ar = np.exp(L)
    s = sum(ar)
    o = []
    for v in L:
        o.append(np.exp(v) / s)
    return o

L=[5,6,7]
print(softmax(L))