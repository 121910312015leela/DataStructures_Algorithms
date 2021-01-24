from sys import stdin
import sys
sys.setrecursionlimit(1000000)

def solve(arr, n, m) :
    graph=[]
    for st in arr:
    	graph.append(list(st))
    word="CODINGNINJA"
    visited=[[False for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='C':
                res=check(graph,word,0,i,j,visited,n,m)
                if res:
                    return 1
    return 0


def check(graph,word,ind,i,j,visited,n,m):
    if ind==len(word):
        return True    
    if i>=n or i<0 or j>=m or j<0:
        return False

    if word[ind]!=graph[i][j] or visited[i][j]:
        return False
    visited[i][j]=True
    
    dirs=[(1,1),(-1,-1),(1,-1),(-1,1),(0,1),(0,-1),(-1,0),(1,0)]
    for x,y in dirs:
        re=check(graph,word,ind+1,i+x,j+y,visited,n,m)
        if re:
            return True
    visited[i][j]=False
    return False
    
        
def takeInput():
    #To take fast I/O
    n,m=list(map(int,stdin.readline().strip().split( )))
    arr = [stdin.readline().strip() for i in range(n)]
    return arr,n,m




# Main 
arr,n,m=takeInput()
print(solve(arr,n,m)) 
