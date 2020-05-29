import matplotlib.pyplot as plt
from random import uniform, seed
import numpy as np
import pandas as pd
import time
from igraph import *
import random
from collections import Counter

def get_RRS(G, p):
    """
    Inputs: G:  Ex2 dataframe of directed edges. Columns: ['source','target']
            p:  Disease propagation probability
    Outputs: A random reverse reachable set expressed as a list of nodes
    """

    source = random.choice(np.unique(G['source']))

    g = G.copy().loc[np.random.uniform(0, 1, G.shape[0]) < p]

    new_nodes, RRS0 = [source], [source]
    while new_nodes:
        temp = g.loc[g['target'].isin(new_nodes)]

        temp = temp['source'].tolist()

        RRS = list(set(RRS0 + temp))

        new_nodes = list(set(RRS) - set(RRS0))

        RRS0 = RRS[:]

    return (RRS)


def RIS(G, k, p=0.5, mc=1000):
    start_time = time.time()
    R = [get_RRS(G, p) for _ in range(mc)]

    SEED = []
    timelapse = []
    for _ in range(k):
        flat_map = [item for subset in R for item in subset]
        seed = Counter(flat_map).most_common()[0][0]
        print(Counter(flat_map).most_common()[0])
        SEED.append(seed)

        R = [rrs for rrs in R if seed not in rrs]

        timelapse.append(time.time() - start_time)

    return (sorted(SEED), timelapse)