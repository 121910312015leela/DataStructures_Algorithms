# Write your code here
import sys
sys.setrecursionlimit(100000)
n,e=map(int,input().split())
graph=[[False for i in range(n)] for i in range(n)]

for i in range(e):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=True
    
visited=[False]*n
def dfs(graph,visited,start,comp):
    comp.append(start)
    visited[start]=True
    for i in range(n):
        if not visited[i] and graph[start][i]:
            # visited[i]=True
            dfs(graph,visited,i,comp)   
while not all(visited):
    comp=[]
    dfs(graph,visited,visited.index(False),comp)
    print(*sorted(comp))
    print()
