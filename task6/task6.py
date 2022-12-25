import numpy as np
import json


def to_json(s):
    js = json.loads(s)
    s1 = []
    for j in js:
        if isinstance(j, list):
            s1.append(j)
        if isinstance(j, str):
            a = []
            a.append(j)
            s1.append(a)
    return s1

def exp_ind(arr, experts):
    ind = -1
    for i in range(len(experts)):
        if arr == experts[i]:
            ind = i
    return ind

def create_matrix(experts, index):
    exp = np.zeros((len(experts[index]), len(experts[index])))
    for i in range(len(experts[index])):
        for j in range(len(experts[index])):
            if experts[index][i] < experts[index][j]:
                exp[i][j] = 1
            if experts[index][i] == experts[index][j]:
                exp[i][j] = 0.5
            if experts[index][i] > experts[index][j]:
                exp[i][j] = 0
    return exp

def task(js):
    experts = to_json(js)
    experts_matrices = []
    for exp in experts:
        experts_matrices.append(create_matrix(experts, exp_ind(exp, experts)))
    
    m = np.zeros(experts_matrices[0].shape)
    for i in range(experts_matrices[0].shape[0]):
        for j in range(experts_matrices[0].shape[0]):
            for k in range(len(experts_matrices)):
                m[i][j] += 1/experts_matrices[k].shape[0] * experts_matrices[k][i][j]

    k0 = []
    for i in range(experts_matrices[0].shape[0]):
        k0.append(1/experts_matrices[0].shape[0])

    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1/l, y)

    while max(abs(k1-k0)) >= 0.001:
        k0 = k1
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1/l, y)

    return k1