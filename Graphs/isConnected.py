# Write your code here
from collections import deque
n,e=map(int,input().split())
graph=[[False for i in range(n)] for j in range(n)]
for i in range(e):
    a,b=map(int,input().split())
    graph[a][b]=True
    graph[b][a]=True
# print(*graph,sep='\n')
# print()
visited=[False]*n

def  bfs(graph,visited,start):
    if n>0:
        d=deque()
        d.append(start)
        visited[start]=True
        while d:
            cur=d.popleft()
            # print(cur,end=' ')
            for i in range(n):
                if not visited[i] and graph[cur][i]:
                    d.append(i)
                    visited[i]=True
                    
bfs(graph,visited,0)        
if not all(visited):
    print("false")
else:
    print('true')
   

    
    
    
# def dfs(graph,visited,start):
#     print(start,end=" ")
#     visited[start]=True
#     for i in range(n):
#         if not visited[i] and graph[start][i]:
#             dfs(graph,visited,i)
# dfs(graph,visited,0)

    
