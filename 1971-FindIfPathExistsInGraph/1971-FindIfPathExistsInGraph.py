# Last updated: 31/10/2026, 19:03:17
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        grid=defaultdict(list) 
        seen=set()
        seen.add(source)

        for u, v in edges:
            grid[u].append(v)
            grid[v].append(u)   

        def dfs(i):
            if i == destination:
                return True

            
            for neigh in grid[i]:
                if neigh not in seen:    
                    seen.add(neigh)
                    if dfs(neigh):
                        return True
            return False

        return dfs(source)            


          