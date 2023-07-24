# BFS (Breadth first Search)
def bfs(adj,source,visited):
    
    q=[]
    visited[source]=True
    q.append(source)
    while q:
        s = q.pop(0)
        print(s,end=" ")
        for u in adj[s]:
            if visited[u]==False:
                visited[u]= True
                q.append(u)
    print()
# BFS for disconnected graph
def bfs_disconnected(adj):
    visited =[False]*len(adj)
    for u in range(len(adj)):
        if visited[u]==False:
            bfs(adj,u,visited)

# BFS (No of connnected components)
def bfs_connected(adj):
    visited=[False]*len(adj)
    count =0
    for u in range(len(adj)):
        if visited[u]==False:
            count+=1
            bfs(adj,u,visited)
    print("count = ",count)

    





#adjaceny list represtation

def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def println(adj):
    for i in range(len(adj)):
        print(i,":",adj[i],end=" ")
    print()

vertex = int(input("Enter no. of vertex: "))
adj =[[] for i in range(vertex)]

while 1:
    c=int(input("Enter 1 to continue else 0 : "))
    if c==0:
        break
    u,v = map(int,input().split())
    addEdge(adj,u,v)
visited = [False]*len(adj)
println(adj)

# bfs(adj,0,visited)
# bfs_disconnected(adj)
bfs_connected(adj)
