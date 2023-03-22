from main import *


def test_dolphins():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/dolphins', 'dolphins.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_football():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/football', 'football.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_karate():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/karate', 'karate.gml')
    G = nx.read_gml(filePath, label='id')
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_krebs():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/krebs', 'krebs.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_adjnoun():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/adjnoun', 'adjnoun.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_lobster():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/lobster', 'lobster.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_netscience():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/netscience', 'netscience.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_polbooks():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/polbooks', 'polbooks.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_shell():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/shell', 'shell.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_star():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data/real/star', 'star.gml')
    G = nx.read_gml(filePath)
    G_copy = G.copy()
    plotNetwork(G, greedyCommunitiesDetection(G_copy, 2))


def test_all():
    test_dolphins()
    test_football()
    test_karate()
    test_krebs()
    test_adjnoun()
    test_lobster()
    test_netscience()
    test_polbooks()
    test_shell()
    test_star()


test_all()
