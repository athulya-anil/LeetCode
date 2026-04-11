# Last updated: 11/04/2026, 16:52:01
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
13                return True
14
15        seen=set()
16        seen.add(source)
17        graph=defaultdict(list)
18
19        for u,v in edges:
20            graph[u].append(v)
21            graph[v].append(u)
22
23        def dfs(i):
24            if i == destination:
25                return True
26            for neigh in graph[i]:
27                if neigh not in seen:
28                    seen.add(neigh)
29                    if dfs(neigh):
30                        return True
31            return(False) 
32        return dfs(source)               
33
34
35