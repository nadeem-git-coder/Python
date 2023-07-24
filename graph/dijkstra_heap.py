import sys
import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for i in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def shortest_path(self, src):
        dist = [float('inf')] * self.vertices
        dist[src] = 0
        visited = [False] * self.vertices
        heap = [(0, src)]

        while heap:
            (d, u) = heapq.heappop(heap)
            if visited[u]:
                continue

            visited[u] = True
            for (v, w) in self.adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        print("Vertex Distance from Source")
        for i in range(self.vertices):
            print("{0}\t\t{1}".format(i, dist[i]))

# Driver program to test methods of graph class
if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = Graph(V)

    # making above shown graph
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    g.shortest_path(0)
