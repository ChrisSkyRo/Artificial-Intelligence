from statistics import mean
import matplotlib.pyplot as plt
import networkx as nx
from fcOptimisation.utils import plotNetwork
from fcOptimisation.utils import modularity
from ga import GA
import os
import warnings
warnings.simplefilter('ignore')


filePaths = []
crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/dolphins', 'dolphins.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/football', 'football.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/krebs', 'krebs.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/adjnoun', 'adjnoun.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/lobster', 'lobster.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/polbooks', 'polbooks.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/shell', 'shell.gml')
filePaths.append(filePath)

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data/real/star', 'star.gml')
filePaths.append(filePath)

for path in filePaths:
    communities_count = 2
    # read network
    G = nx.read_gml(path)
    # get network properties
    mat = nx.adjacency_matrix(G)
    matrix = [[0] * len(G.nodes) for _ in range(len(G.nodes))]
    tmp = mat.nonzero()
    for i in range(len(tmp[0])):
        matrix[tmp[0][i]][tmp[1][i]] = 1
    net = {
        'noNodes': len(G.nodes),
        'mat': matrix,
        'noEdges': len(G.edges),
        'degrees': [degree[1] for degree in G.degree()]
    }
    averageValues = []
    minimumValues = []
    maximumValues = []
    yPoints = []

    # initialise de GA parameters
    gaParam = {'popSize': 100, 'noGen': 1000}
    # problem parameters
    prbParam = {'min': 1, 'max': communities_count, 'function': modularity, 'noDim': net['noNodes'], 'net': net}
    # initialize GA
    ga = GA(gaParam, prbParam)
    ga.initialisation()
    ga.evaluation()
    bestChromosomes = []
    generations = gaParam['noGen']
    population = gaParam['popSize']

    # start simulation
    for g in range(generations):
        ga.oneGeneration()
        # store best chromosome for each generation in a list
        best = ga.bestChromosome()
        bestChromosomes.append(best)
        maximumValues.append(best.fitness)
        minimumValues.append(ga.worstChromosome().fitness)
        averageValues.append(mean([x.fitness for x in ga.population]))
        yPoints.append(len(yPoints))

    plt.plot(yPoints, minimumValues, label="Minimum")
    plt.plot(yPoints, averageValues, label="Average")
    plt.plot(yPoints, maximumValues, label="Maximum")
    plt.legend()
    plt.show()

    # search for the best chromosome
    bestChromo = sorted(bestChromosomes, key=lambda x: x.fitness, reverse=True)[:population][0]
    # plot the network
    plotNetwork(G, bestChromo.repres)
