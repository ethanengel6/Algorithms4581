#[[0, -1], [1, 0], [3, 1], [2, 3], [5, 3], [4, 5], [7, 1], [6, 0]]

def mst(g):
    origin=0
    mstEdges=[[origin,-1]]
    nVerts = len(g)
    vertsProcessed = [None]*nVerts
    numVertsProcessed = 0
    vertsProcessed[origin] = 1

    while (numVertsProcessed < nVerts- 1):
        minimum = float('inf')
        EdgeEnd = 0
        EdgeEnd2 = 0
        for i in range(nVerts):
            if vertsProcessed[i]==1:
                for j in range(nVerts):
                    if ((not vertsProcessed[j]) and g[i][j]):
                        if minimum > g[i][j]:
                            minimum = g[i][j]
                            EdgeEnd = i
                            EdgeEnd2 = j
        mstEdges.append([EdgeEnd,EdgeEnd2])
        vertsProcessed[EdgeEnd2] = 1
        numVertsProcessed += 1
    print(mstEdges)

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
[7, 0, 12, 5, 0, 0, 0, 9],
[0, 12, 0, 6, 0, 0, 0, 0],
[0, 5, 6, 0, 14, 8, 0, 0],
[0, 0, 0, 14, 0, 3, 0, 0],
[10, 0, 0, 8, 3, 0, 0, 0],
[15, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 0, 0, 0, 0, 0, 0]]
mst(graph)
