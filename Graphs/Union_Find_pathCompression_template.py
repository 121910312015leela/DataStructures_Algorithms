class DSU:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)
        self.rank = [0 for _ in range(n + 1)]

    def union(self, u, v):
        # union by ranking
        if self.rank[u] > self.rank[v]:
            self.parents[v] = u
        else:
            self.parents[u] = v
        self.rank[u] += self.rank[v]
        self.rank[v] = self.rank[u]

    def find(self, v):
        start_node = v
        while self.parents[v] != -1:
            v = self.parents[v]
        # Path compression
        if start_node != v:
            self.parents[start_node] = v
        return v
        
