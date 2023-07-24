from typing import List, Tuple
import sys

class Graph:
    def __init__(self, V: int) -> None:
        self.V = V
        self.adj = [set() for _ in range(V)]

    def addEdge(self, u: int, v: int, w: int) -> None:
        self.adj[u].add((v, w))
        self.adj[v].add((u, w))

    def shortestPath(self, src: int) -> None:
        # Create a set to store vertices that are being processed
        setds = set()

        # Create a list for distances and initialize all distances as infinite
        dist = [sys.maxsize] * self.V

        # Insert source itself in Set and initialize its distance as 0
        setds.add((0, src))
        dist[src] = 0

        # Loop until all shortest distance are finalized
        while setds:
            # The first vertex in Set is the minimum distance vertex, extract it from set
            tmp = setds.pop(0)

            # vertex label is stored in second of pair (it has to be done this way to keep the vertices sorted by distance)
            u = tmp[1]

            # Get all adjacent vertices of a vertex
            for v, weight in self.adj[u]:
                # If there is a shorter path to v through u
                if dist[v] > dist[u] + weight:
                    # If distance of v is not infinite then it must be in our set, so removing it and inserting again with updated less distance
                    if dist[v] != sys.maxsize:
                        setds.remove((dist[v], v))

                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    setds.add((dist[v], v))

        # Print shortest distances stored in dist[]
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

# Driver program to test methods of graph class
if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = Graph(V)

    # making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    g.shortestPath(0)
