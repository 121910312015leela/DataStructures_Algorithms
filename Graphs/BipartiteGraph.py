# check if the given graph (adjacency list) is bipartite or not

BP={'1':set(),'0':{0}}
# the two sets / groups of vertices
pending=[0]
# this contains the vertices which have been visited but their nbrs have not been processed

while pending:
    # get a vertex
    cur=pending.pop()
    # check which set it belongs
    curset= 0 if cur in BP['0'] else 1
    
    # check all its neighbours
    
    for nbr in graph[cur]:
        # the neighbour is not present in any of the sets i.e good candidate
        if nbr not in BP['0'] and nbr not in BP['1']:
            BP[str(1-curset)].add(nbr)
            #add nbr the opposite set as that of its parent
            pending.append(nbr)
        elif nbr  in BP[str(curset)]:  return False
        # if that nbr is  already present in the set from which the parent came
        # then its a bad candidate for BP graph hence such graph is not BP
return True
