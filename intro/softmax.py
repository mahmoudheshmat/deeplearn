import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    denom = sum(np.exp(L))
    results = []
    for number in L:
        results.append(np.exp(number) / denom)
    return results