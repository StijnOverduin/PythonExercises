from Excercises9Feb import createCompleteGraph
from graph_io import*
from graph import*

def makeComplement():
    newGraph = Graph(False)
    with open('toBeComplemented.gr') as f:
        G = load_graph(f)

    for v in G.vertices:
        ver = Vertex(newGraph)
        newGraph.add_vertex(ver)
        for v2 in G.vertices:
            if not G.is_adjacent(v, v2):
                e = Edge(v, v2)
                newGraph.add_edge(e)
    with open('complemented', 'w') as f:
        save_graph(newGraph, f)
