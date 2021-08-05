def loadGraph(edgeFilename):
    f= open(edgeFilename, "r")
    largestVertex =-1
    list_of_lists = []
    for line in f:
        stripped_line = line. strip()
        line_list = stripped_line. split()
        list_of_lists. append(line_list)
        if int(line_list[0])>largestVertex:
            largestVertex=int(line_list[0])
        if int(line_list[1])>largestVertex:
            largestVertex=int(line_list[1])
    adjList = [ []  for v in range(largestVertex + 1)]
    for zz in range (len(list_of_lists)):
        vert_a = int(list_of_lists[zz][0])
        vert_b = int(list_of_lists[zz][1])
        adjList[vert_a].append(vert_b)
        adjList[vert_b].append(vert_a)
    f.close()
    return adjList


class MyQueue:
    def __init__(self):
        self.items = []

    def __str__ (self):
        'MyQueue('+ str(self.items) +')'

    def empty(self):
         return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
         return self.items.pop()


def BFS(G, s):
    visited=[]
    distanceList=[-1]*len(G)
    visited_boolean = [False]*len(G)
    parent=[None]*len(G)
    q=MyQueue()

    visited_boolean[s]=True
    distanceList[s]=0
    q.enqueue(s)
    while not q.empty():
        current = q.dequeue()
        visited.append(current)

        for v in G[current]:
            if not visited_boolean[v]:
                visited_boolean[v]=True
                parent[v]=current
                distanceList[v]=distanceList[current]+1
                q.enqueue(v)

    return(distanceList)

def distanceDistribution(G):
    distDict={}
    for dd in range(max(G)+1):
        distDict[dd] = round(G.count(dd)/(len(G))*100,2)
    print(distDict)
    return distDict



distanceDistribution(BFS(loadGraph("edges.txt"),1234))
#{0: 0.02, 1: 0.22, 2: 25.65, 3: 40.63, 4: 27.06, 5: 2.9, 6: 3.52}
#distanceDistribution(BFS(loadGraph("edges.txt"),0))
#{0: 0.02, 1: 8.59, 2: 28.99, 3: 43.13, 4: 12.85, 5: 2.9, 6: 3.52}
#distanceDistribution(BFS(loadGraph("edges.txt"),2000))
#{0: 0.02, 1: 0.82, 2: 17.88, 3: 6.12, 4: 55.34, 5: 14.73, 6: 1.58, 7: 3.52}
#distanceDistribution(BFS(loadGraph("edges.txt"),3000))
#{0: 0.02, 1: 2.25, 2: 17.36, 3: 25.7, 4: 37.04, 5: 16.27, 6: 1.36}
#distanceDistribution(BFS(loadGraph("edges.txt"),4000))
#{0: 0.02, 1: 0.22, 2: 1.24, 3: 0.1, 4: 6.51, 5: 45.88, 6: 40.93, 7: 1.58, 8: 3.52}

#The SWP was run five times with different source nodes.  The vast majority of the time, the distances from the source node are <=6.
#As the output shows, there were exceptions, some sevens & even a couple of eights.
#The majority of distances from the source node are between 2 & 4, inclusive.
