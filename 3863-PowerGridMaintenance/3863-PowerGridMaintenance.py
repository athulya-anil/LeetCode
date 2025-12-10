# Last updated: 10/12/2025, 07:39:35
from collections import defaultdict
import heapq

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: 
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        # Group stations by component root
        comps = defaultdict(list)
        for node in range(1, c + 1):
            root = dsu.find(node)
            comps[root].append(node)

        # Build a min-heap of online nodes per component
        online_heap = {}
        for root, nodes in comps.items():
            online_heap[root] = nodes[:]
            heapq.heapify(online_heap[root])

        online = [True] * (c + 1)
        res = []

        for t, x in queries:
            root = dsu.find(x)
            if t == 1:
                if online[x]:
                    res.append(x)
                else:
                    # Pop offline ones from top
                    while online_heap[root] and not online[online_heap[root][0]]:
                        heapq.heappop(online_heap[root])
                    res.append(online_heap[root][0] if online_heap[root] else -1)
            else:  # type 2
                online[x] = False

        return res
