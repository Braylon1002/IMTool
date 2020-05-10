import matplotlib.pyplot as plt
from random import uniform, seed
import numpy as np
import pandas as pd
import time
from igraph import *
import random
from collections import Counter


def IC(g, S, p=0.5, mc=1000):
    """
    input
    g: the graph you input
    S: seed set
    p: Activation limits
    mc: Number of cycles of Monte Carlo

    output
    the Influence of current seed set
    """
    spread = []
    for i in range(mc):
        new_active, A = S[:], S[:]
        while new_active:
            new_ones = []
            for node in new_active:
                np.random.seed(i)
                success = np.random.uniform(0, 1, len(g.neighbors(node, mode='out'))) < p
                new_ones += list(np.extract(success, g.neighbors(node, mode='out')))

            new_active = list(set(new_ones) - set(A))

            A += new_active

        spread.append(len(A))

    return np.mean(spread)


def greedy(g, k, p=0.1, mc=1000):
    """
    input
    g: the graph you input
    k: number of nodes in influence maximization set
    p: Activation limits
    mc: Number of cycles of Monte Carlo

    output
    influence maximization set
    spread of each node
    time cost
    """
    S, spread, timelapse, start_time = [], [], [], time.time()
    for _ in range(k):
        spread_mem, node_mem = -1, -1
        for i in set(range(g.vcount())) - set(S):

            s = IC(g, S + [i], p, mc)

            if s > spread_mem:
                spread_mem = s
                node_mem = i

        S.append(node_mem)
        spread.append(spread_mem)
        timelapse.append(time.time() - start_time)
    return (S, spread, timelapse)