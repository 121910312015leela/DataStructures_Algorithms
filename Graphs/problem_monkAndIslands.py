## Read input as specified in the question.
## Print output as specified in the question.
from collections import deque
import sys
sys.setrecursionlimit(100000)
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited=[False]*(n+1)
    visited[0]=True
    d=deque()
    d.append(1)
    visited[1]=True
    
    lvl=[0]*(n+1)
    
    while d:
        cur=d.popleft()
        for v in graph[cur]:  
            if not visited[v]:
                d.append(v)
                visited[v]=True
                lvl[v]=lvl[cur]+1
    print(lvl[n])
            
        
        
