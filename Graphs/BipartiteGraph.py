# check if the given graph (adjacency list) is bipartite or not

BP={'1':set(),'0':{0}}
pending=[0]
while pending:

    cur=pending.pop()
    curset= 0 if cur in BP['0'] else 1
    
    for nbr in graph[cur]:
        if nbr not in BP['0'] and nbr not in BP['1']:
            BP[str(1-curset)].add(nbr)
            pending.append(nbr)
        elif nbr not in BP[str(1-curset)]:  return False
        
return True
