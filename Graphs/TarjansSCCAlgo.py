# adj the adjacency list representation of the graph
    # V is the number of vertices in the graph
    def tarjans(self,n,adj):
        # code here
        disc=[-1]*n
        low=[-1]*n
        inStc=[False]*n
        stc=[]
        time=[0]
        allSCC=[]
        def dfs(u):
            disc[u]=low[u]=time[0]
            time[0]+=1
            stc.append(u)
            inStc[u]=True
            
            for v in adj[u]:
                if disc[v]==-1:
                    dfs(v)
                    low[u]=min(low[u],disc[v])
                elif (inStc[v]):
                    low[u]=min(low[u],disc[v])
            scc=[]
            if low[u]==disc[u]:
                print('SCC is: ',end=" ")
                while stc and stc[-1]!=u:
                    node=stc.pop()
                    print(node)
                    scc.append(node)
                    inStc[node]=False 
                node=stc.pop()
                print(node)
                scc.append(node)
                inStc[node]=False
            allSCC.append(sorted(scc))
        for i in range(n):
            if disc[i]==-1:dfs(i)
        print(allSCC)
        return sorted(allSCC)
        
