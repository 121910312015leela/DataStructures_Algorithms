# my editorial https://binarysearch.com/problems/Edges-that-Disconnect-the-Graph/editorials/3980208 
 def solve(self, GG):
        n = len(GG)
        graph = defaultdict(list)
        for i, ele in enumerate(GG):
            graph[i] += ele
        # print(graph)
        seenAt, lowest_link, parent = ([-1] * n, [-1] * n, [-1] * n)
        bridges = []

        def tarjans(u, time):
            seenAt[u] = lowest_link[u] = time
            for v in graph[u]:
                if seenAt[v] == -1:
                    parent[v] = u
                    tarjans(v, time + 1)
                    lowest_link[u] = min(lowest_link[u], lowest_link[v])
                    if lowest_link[v] > seenAt[u]:
                        bridges.append((u, v))
                elif v != parent[u]:
                    lowest_link[u] = min(lowest_link[u], seenAt[v])

        for i in range(n):
            if seenAt[i] == -1:
                tarjans(i, 0)
        # print(*bridges)
        return len(bridges)
