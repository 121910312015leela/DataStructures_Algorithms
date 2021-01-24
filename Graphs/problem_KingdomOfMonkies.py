import sys
sys.setrecursionlimit(1000000)

def dfs(graph,start,visited,comp):
    if visited[start]: return
    visited[start]=True
    comp.append(start)
    for v in graph[start]:
        if not visited[v]:
            dfs(graph,v,visited,comp)     
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    arr=[0]+[int(i) for i in input().split()]
    visited=[False]*(n+1)
    visited[0]=True
    ma=0
    for i in range(n+1):
        if not visited[i]:
            comp=[]
            dfs(graph,i,visited,comp)
            compscore=sum([arr[c] for c in comp])
            ma=max(ma,compscore)
    print(ma)
    
    

    
