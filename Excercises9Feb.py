from graph import*

def createGraph(n):
    G = Graph(False, int(n))
    for i in range(0, len(G.vertices) - 1):
        u = Edge(G.vertices[i], G.vertices[i+1])
        G += u
    return G


def createCycleGraph():
    G = Graph(False, 4)
    for i in range(0, len(G.vertices)):
        if i == len(G.vertices) - 1:
            u = Edge(G.vertices[i], G.vertices[0])
            G += u
        else:
            u = Edge(G.vertices[i], G.vertices[i+1])
            G += u
    return G



def createCompleteGraph(object):
    G = object
    for i in G.vertices:
        for v in G.vertices:
            if i != v and not G.is_adjacent(i, v):
                e = Edge(i, v)
                G.add_edge(e)
    return G


