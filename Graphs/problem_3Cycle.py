# Write your code here
import sys
from collections import deque
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
graph=[[False for i in range(n)] for j in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=True
# print(*graph,sep='\n')  
seenCycles=set()
count=0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            for k in range(n):
                if graph[j][k]:
                    if graph[i][k] and frozenset({i,j,k}) not in seenCycles:
                        count+=1
                        seenCycles.add(frozenset({i,j,k}))
print(count)
            
# def bfs(graph,seenCycles,start=0,seenCycles):
#     d.append(start)
#     visited[start]=True
#     while d:
#         cur=d.popleft()
#         for i in range(n):
#             if visited[i] and graph[cur][i]:
#                 visited[i]=True
#                 d.append(i)
#     	for num in d:
            
        
                
                

    
