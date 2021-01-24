t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    src=input().split()
    dst=input().split()
    graph=[[] for i in range(n+1)]
    for i in range(q):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited=[False]*(n+1)
    def dfs(visited,graph,ind,comp):
        if visited[ind]: return 
        comp.append(ind)
        visited[ind]=True
        for nbr in graph[ind]:
            if not visited[nbr]:dfs(visited,graph,nbr,comp)               
    all_comps=[]         
    for i in range(n+1):
        comp=[]
        if not visited[i]:
            dfs(visited,graph,i,comp)
            all_comps.append(comp)
    all_comps.pop(0)
    ans=True
    for ll in all_comps:
        srcChars=set()
        dstChars=set()
        for i in ll:
            srcChars.add(src[i-1])
            dstChars.add(dst[i-1])
        ans&=srcChars==dstChars
    if ans:print('YES')
    else:print("NO")
        
    

        
        
    
                
            
        
    
    
    
    
    
    
    
    
