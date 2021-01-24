# Write your code here
import sys
sys.setrecursionlimit(10**6)
def getPair():
    return map(int,input().split())
n,e=getPair()
graph=[[False for i in range(n)] for j in range(n)]
for i in range(e):
    a,b=getPair()
    graph[a][b]=graph[b][a]=True  
s,e=getPair()

path=[]
visited=[False]*n
print(*graph,sep="\n")
def dfs(graph,visited,s,e):
    path=[]
    if s==e: return path
    visited[s]=True
    for i in range(n):
        if not visited[i] and graph[s][i]:
            visited[i]=True 
            re=dfs(graph,visited,i,e)
            if re!=None:
                path+=re
                path.append(i)
                return path
path=dfs(graph,visited,s,e)
if path:
    path+=[s]
    for i in path:sssssssss
    	print(i,end=" ")
	
