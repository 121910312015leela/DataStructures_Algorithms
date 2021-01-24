# Write your code here


def getAns(graph,visited,i,j,n):
    if i>=n or j>=n or i<0 or j<0:
        return 0
    if visited[i][j]:
        return 0
    if graph[i][j]!=1:
        return 0
    visited[i][j]=True
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
    re=0
    for x,y in dir:
        re+=getAns(graph,visited,i+x,j+y,n)
    return 1+re
    visited[i][j]=False

n=int(input())
graph=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    graph.append(l)
# print(*graph,sep='\n')
visited=[[False for i in range(n)] for j in range(n)]
ma=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            Len=getAns(graph,visited,i,j,n)
            # print(Len)
            ma=max(ma,Len)
print(ma)


    
