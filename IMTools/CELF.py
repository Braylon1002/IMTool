import matplotlib.pyplot as plt
from random import uniform, seed
import numpy as np
import pandas as pd
import time
from igraph import *
import random

from IMTools.MonteCarloIC_greedy import IC


def celf(g, k, p=0.1, mc=1000):
    start_time = time.time()
    margin_gain = [IC(g, [v], p, mc) for v in range(g.vcount())]

    Q = sorted(zip(range(g.vcount()), margin_gain), key=lambda x: x[1], reverse=True)

    S, spread, SPREAD = [Q[0][0]], Q[0][1], [Q[0][1]]
    Q = Q[1:]
    LOOKUPS = [g.vcount()]
    timelapse = [time.time() - start_time]

    for _ in range(k - 1):
        check, node_lookup = False, 0

        while not check:
            node_lookup += 1

            current = Q[0][0]

            Q[0] = (current, IC(g, S + [current], p, mc) - spread)

            Q = sorted(Q, key=lambda x: x[1], reverse=True)

            check = (Q[0][0] == current)

        spread = Q[0][1]
        S.append(Q[0][0])
        SPREAD.append(spread)
        LOOKUPS.append(node_lookup)
        timelapse.append(time.time() - start_time)

        Q = Q[1:]

    return (S, SPREAD, timelapse, LOOKUPS)