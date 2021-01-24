from sys import stdin
import sys
sys.setrecursionlimit(1000000)
def solve(arr, n, m) :
    # Write your code here
    graph=[]
    k=4
    visited=[[False for i in range(m)] for j in range(n)]
    for s in arr:
        graph.append(list(s)) 
    for i in range(n):
        for j in range(m):
            print(graph[i][j])
            if check(graph,i,j,visited,i,j,n,m,0,k):return True
    return False


def check(graph,i,j,visited,curStart,curEnd,n,m,L,k):
    if i==curStart and j==curEnd and L>=k:return True
    if i>=n or i<0 or j>=m or j<0: return False
    if graph[i][j]!=graph[curStart][curEnd]: return False
    if visited[i][j]:return False
    visited[i][j]=True
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]
    for x,y in dirs:
        re=check(graph,i+x,j+y,visited,curStart,curEnd,n,m,L+1,k)
        if re: return True
    visited[i][j]=False
    return False


def takeInput():
    #To take fast I/O
    n,m=list(map(int,stdin.readline().strip().split( )))
    arr = [stdin.readline().strip() for i in range(n)]
    return arr,n,m




# Main 
arr,n,m = takeInput()
ans = solve(arr,n,m)

if(ans) :
    print('true')
else :
    print('false')
