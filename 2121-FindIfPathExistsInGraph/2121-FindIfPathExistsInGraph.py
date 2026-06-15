# Last updated: 14/06/2026, 23:01:40
from collections import defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        graph=defaultdict(list)
        seen=set()
        seen.add(source)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i):
            if i == destination:
                return True

            for neigh in graph[i]:
                if neigh not in seen:
                    seen.add(neigh)
                    if dfs(neigh):
                        return True
            return(False)   
        return dfs(source)            
                


