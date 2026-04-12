# Last updated: 12/04/2026, 12:48:07
1from collections import defaultdict
2
3class Solution(object):
4    def validPath(self, n, edges, source, destination):
5        """
6        :type n: int
7        :type edges: List[List[int]]
8        :type source: int
9        :type destination: int
10        :rtype: bool
11        """
12        if source == destination:
13            return True
14
15        graph=defaultdict(list)
16        seen=set()
17        seen.add(source)
18
19        for u,v in edges:
20            graph[u].append(v)
21            graph[v].append(u)
22
23        def dfs(i):
24            if i == destination:
25                return True
26
27            for neigh in graph[i]:
28                if neigh not in seen:
29                    seen.add(neigh)
30                    if dfs(neigh):
31                        return True
32            return(False)   
33        return dfs(source)            
34                
35
36
37