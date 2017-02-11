from graph_io import*
from graph import*

def makeComplement():

    done = {}
    with open('toBeComplemented.gr') as f:
        G = load_graph(f)
        newGraph = Graph(G.directed)
        for v in G.vertices:
            if v not in done:
                u = Vertex(newGraph, v)
                newGraph.add_vertex(u)
                done[v] = u
            for v2 in G.vertices:
                if v2 not in done:
                    u2 = Vertex(newGraph, v2)
                    newGraph.add_vertex(u2)
                    done[v2] = u2
                if not G.is_adjacent(v, v2) and v != v2:
                    e = Edge(done[v], done[v2])
                    newGraph.add_edge(e)




    with open('complemented', 'w') as f:
        save_graph(newGraph, f)


makeComplement()