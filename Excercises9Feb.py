from graph import*

def createGraph():
    G = Graph(False, 4)
    for i in range(0, len(G.vertices) - 1):
        u = Edge(G.vertices[i], G.vertices[i+1])
        G += u
    return G

print("n Graph: n-1 length")
print(createGraph())

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

print("n Cycle")
print (createCycleGraph())

