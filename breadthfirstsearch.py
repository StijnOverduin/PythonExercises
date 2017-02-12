from graph import*
from graph_io import*
from visualiseGraph import fromGraph
from Excercises9Feb import createGraph

frontier = []
order = {}
G = Graph(False)
V = Vertex(G)

def bfs(graph, start):
    count = 0
    order ={}
    queue = []
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for i in v.neighbours:
            if i not in order:
                queue.append(i)

        if v not in order:
            order[v] = count
            count += 1
    for vertex in graph.vertices:
        if vertex in order:
            vertex.label = order[vertex]

    return graph

# with open('examplegraph.gr') as f:
#    GG = load_graph(f)
# fromGraph(bfs(GG, GG.vertices[0]))

GG = createGraph(10)
fromGraph(bfs(GG, GG.vertices[0]))
print(bfs(GG, GG.vertices[0]))

def dfs(graph, start):
    count = 0
    order ={}
    stack = []
    stack.append(start)
    while stack:
        v = stack.pop()
        i = v.neighbours[0]
        if i not in order:
            stack.append(i)

        if v not in order:
            order[v] = count
            count += 1
    for vertex in graph.vertices:
        if vertex in order:
            vertex.label = order[vertex]

    return graph


