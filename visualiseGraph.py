from graph_io import*


def fromFile():
    with open('examplegraph.gr') as f:
        G = load_graph(f)

    with open('mygraph.dot', 'w') as f:
        write_dot(G, f)


def fromGraph(graph):
    with open("mygraph1.dot", 'w') as f:
        write_dot(graph, f)