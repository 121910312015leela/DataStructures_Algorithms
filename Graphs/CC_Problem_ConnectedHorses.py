## Read input as specified in the question.
## Print output as specified in the question.

import math
import sys
sys.setrecursionlimit(1000000)
t=int(input())

def moveHorse(i,j,board,n,m,comps):
    if board[i][j]!="H":
        return 
    board[i][j]='V'
    comps.append('*')
    dirs=[(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for x,y in dirs:
        if (i+x >0 and i+x <=n ) and (j+y>0 and j+y<=m):
            moveHorse(i+x,j+y,board,n,m,comps)
 

for i in range(t):
    
    n,m,q=map(int,input().split())
    board=[[ '_' for i in range(m+1)] for j in range(n+1)]
    for i in range(q):
        x,y=map(int,input().split())
        board[x][y]='H'       
    # print(*board,sep='\n')
    MOD=10**9+7
    ans=1
    for i in range(n):
        for j in range(m):
            comps=[]
            if board[i][j]=="H":
                moveHorse(i,j,board,n,m,comps)
                # print(comps)
                ans*=(math.factorial(len(comps))) %MOD
    print(ans%MOD)
                
    
    
        
