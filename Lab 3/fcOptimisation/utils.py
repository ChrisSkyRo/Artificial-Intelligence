from random import uniform
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def generateNewValue(lim1, lim2):
    return uniform(lim1, lim2)


def binToInt(x):
    val = 0
    # x.reverse()
    for bit in x:
        val = val * 2 + bit
    return val


# plot a network
def plotNetwork(G, communities):
    np.random.seed(123)  # to freeze the graph's view (networks uses a random view)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(16, 8))
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos)
    plt.show()


def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if communities[i] == communities[j]:
               Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M


def modularity_density(communities, param, myLambda=0.5):
    G = nx.from_numpy_matrix(np.matrix(param['mat']))
    my_communities = [[] for _ in range(param['noNodes'])]
    for i in range(param['noNodes']):
        my_communities[communities[i] - 1].append(i)
    Q = 0.0
    for community in my_communities:
        sub = nx.subgraph(G, community)
        sub_n = sub.number_of_nodes()
        interior_degrees = []
        exterior_degrees = []
        for node in sub:
            interior_degrees.append(sub.degree(node))
            exterior_degrees.append(G.degree(node) - sub.degree(node))
        try:
            Q += (1 / sub_n) * (
                        (2 * myLambda * np.sum(interior_degrees)) - (2 * (1 - myLambda) * np.sum(exterior_degrees)))
        except ZeroDivisionError:
            pass
    return Q


def z_modularity(communities, param):
    G = nx.from_numpy_matrix(np.matrix(param['mat']))
    my_communities = [[] for _ in range(param['noNodes'])]
    for i in range(param['noNodes']):
        my_communities[communities[i] - 1].append(i)
    edges = G.number_of_edges()
    Q = 0.0
    mmc = 0
    dc2m = 0
    for community in my_communities:
        sub = nx.subgraph(G, community)
        sub_n = sub.number_of_nodes()
        dc = 0
        for node in sub:
            dc += G.degree(node)
        mmc = sub_n / edges
        dc2m += (dc / (2 * edges)) ** 2
    try:
        Q = (mmc - dc2m) / np.sqrt(dc2m * (1 - dc2m))
    except ZeroDivisionError:
        pass
    return Q