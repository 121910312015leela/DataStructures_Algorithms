## Read input as specified in the question.
## Print output as specified in the question. 

             # getting the input
n,e=map(int,input().split())
adj=[[0 for i in range(n)] for i in range(n)]
for i in range(e):
    x,y,w=map(int,input().split())
    adj[x][y]=w
    adj[y][x]=w

    # initializations 
parent=[-1]*n
weight=[float('inf')]*n
visited=[False]*n
weight[0]=0
parent[0]=0

#-------------------------------------

def getMin(weight,visited):
    minVert=-1
    for i in range(0,len(visited)):
        if (not visited[i] and (minVert==-1 or(weight[minVert]>weight[i]))):
        	minVert=i
    return minVert


for j in range(n):
    minEdge=getMin(weight,visited)
    # print(minEdge)
    visited[minEdge]=True
    
    for i in range(n):
        if adj[minEdge][i]>0 and not visited[i]:
            if adj[minEdge][i]<weight[i]:
                weight[i]=adj[minEdge][i]
                parent[i]=minEdge
    
for i in range(1,n):
    k=min(parent[i],i)
    s=parent[i]+i
    print(k,s-k,weight[i])

