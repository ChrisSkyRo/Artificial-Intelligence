# prerequisites
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings

from networkx.algorithms import community

warnings.simplefilter('ignore')


# plot a network
def plotNetwork(G, communities):
    np.random.seed(123)  # to freeze the graph's view (networks uses a random view)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(16, 8))
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=list(communities.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos)
    plt.show()


def greedyCommunitiesDetection(G, communities_count=2):
    # Input: a graph
    # Output: list of community index (for every node)
    communities = dict.fromkeys(G.nodes, 0)
    connected_components = nx.algorithms.components.number_connected_components(G)
    while connected_components < communities_count and G.number_of_edges():
        # calculate betweeness for each edge of the graph
        betweenness = nx.algorithms.centrality.edge_betweenness_centrality(G)
        # sort edges by betweenness
        sorted_edges = sorted(betweenness.items(), key=lambda item: item[1], reverse=True)
        print(sorted_edges)
        # remove edge with the highest betweenness
        G.remove_edge(*sorted_edges[0][0])
        connected_components = nx.algorithms.components.number_connected_components(G)
    # mark each community with a different number
    connected_components = list(nx.components.connected_components(G))
    community = 1
    for component in connected_components:
        for node in component:
            communities[node] = community
        community += 1

    return communities
