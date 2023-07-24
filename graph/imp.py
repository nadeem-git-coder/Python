#adjaceny list represtation

def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def println(adj):
    print([i for i in adj])

vertex = int(input("Enter no. of vertex: "))
adj =[[] for i in range(vertex)]

while 1:
    c=int(input("Enter 1 to continue else 0 : "))
    if c==0:
        break
    u,v = map(int,input().split())
    addEdge(adj,u,v)

println(adj)