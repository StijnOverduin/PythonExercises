from graph_io import*
from graph import*


def modifyGraph():
    with open('examplegraph.gr') as f:
        G = load_graph(f)
    v = Vertex(G)
    u = Vertex(G)
    G.add_vertex(v)
    G.add_vertex(u)

    e = Edge(v, u)
    f = Edge(G.vertices[0], v)
    G.add_edge(e)
    G.add_edge(f)

    with open('examplegraph2.gr', 'w') as f:
        save_graph(G, f)


modifyGraph()