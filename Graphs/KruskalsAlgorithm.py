## Read input as specified in the question.
## Print output as specified in the question.
from heapq import heappop,heappush,heapify

# ------------- getting the input----------------
n,e=map(int,input().split())
graph=[]
heapify(graph)
for i in range(e):
    x,y,w=map(int,input().split())
    heappush(graph,(w,x,y))
# print(list(graph))

# algo----------------------------

def getParent(node,parent):
    if node==parent:
        return node
    parent[node]=getParent(parent[node],parent)
    return parent[node]

def find(x,y,parent):
    parentX=getParent(x,parent)
    parentY=getParent(y,parent)
    res=True
    if parentX!=parentY:
        res=False
        parent[parentX]=parentY
    return res
    
    
parent=[i for i in range(n)]
count=0
ans=[]
while count<n-1:
    w,x,y=heappop(graph)
    if not find(x,y,parent):
        ans.append((x,y,w))
        count+=1
# print(ans)
for x,y,z in ans[::-1]:
    x,y=sorted([x,y])
    print(x,y,z)
        
        
	
