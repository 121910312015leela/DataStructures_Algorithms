## Read input as specified in the question.
## Print output as specified in the question.
import sys
sys.setrecursionlimit(1000000)

def dfs(graph,start,visited,stc,comp):
    
    # dfs for first operation
    visited[start]=True
    if stc=='two':
        comp.append(start)  
    for v in graph[start]:
        if not visited[v]:
            dfs(graph,v,visited,stc,[])        
    if comp=='one':
    	stc.append(start)
        
        
def kosa(graph,graphT,visited):
    
    # first iteration -- adding the vertices to stack
    stc=[]
    for i in range(1,n+1):
        if not visited[i]:
        	dfs(graph,i,visited,stc,"one")
    # print(stc)
            
	# second operation -- performing on stack and graphT
    count=0
    visited=[False]*(n+1)
    visited[0]=True
    while stc:
        cur=stc.pop()
        if not visited[cur]:
            comp=[]
            dfs(graphT,cur,visited,'two',comp)
            count+=1
    # print(*SCC,sep='\n')
    return count


t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    graph=[[] for j in range(n+1)]
    graphT=[[] for j in range(n+1)]
    visited=[False]*(n+1)
    visited[0]=True
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        graphT[y].append(x)
    print(kosa(graph,graph,visited))
    
    
    
