import operator
import numpy as np
import copy
import time

def LFA(matrix):
    n = len(matrix)
    Mr = [1 for i in range(n)]
    for i_ in range(1, n):
        i = n - i_
        for j in range(0, i + 1):
            Mr[j] = Mr[j] + matrix[j][i] * Mr[i]
            Mr[i] = (1 - matrix[j][i]) * Mr[i]
    return Mr

def IMRank(matrix):
    start = time.clock()
    t = 0
    r0 = [i for i in range(len(matrix))]
    r = [0 for i in range(len(matrix))]
    while(True):
        t = t + 1
        r = LFA(matrix)
        r = np.argsort(-np.array(r))
        if operator.eq(list(r0), list(r)):
            break
        r0 = copy.copy(r)
    print('运行时间 ： {}'.format(time.clock() - start))
    print(r)