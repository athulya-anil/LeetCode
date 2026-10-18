# Last updated: 18/10/2026, 14:37:53
1from collections import defaultdict
2class Solution:
3    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
4        if source == destination:
5            return True
6        grid=defaultdict(list) 
7        seen=set()
8        seen.add(source)
9
10        for u, v in edges:
11            grid[u].append(v)
12            grid[v].append(u)   
13
14        def dfs(i):
15            if i == destination:
16                return True
17
18            
19            for neigh in grid[i]:
20                if neigh not in seen:    
21                    seen.add(neigh)
22                    if dfs(neigh):
23                        return True
24            return False
25
26        return dfs(source)            
27
28
29          