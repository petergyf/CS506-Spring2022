import numpy as np

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if len(x) == 0 and len(y) == 0:
        return "lengths must not be zero"
    a = set(x)
    b = set(y)
    # calucate jaccard similarity
    j = 1 - float(len(a.intersection(b))) / len(a.union(b))
    return j

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0:
        return "lengths must not be zero"
    if len(x) != len(y):
        return "lengths must be equal"
    return np.dot(x, y)/(np.linalg.norm(x)*np.linalg.norm(y))

# Feel free to add more
