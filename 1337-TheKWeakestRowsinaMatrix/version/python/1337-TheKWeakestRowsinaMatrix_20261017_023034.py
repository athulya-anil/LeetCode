# Last updated: 17/10/2026, 02:30:34
1import heapq
2class Solution:
3    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
4        soldiers = []
5
6        for i,row in enumerate(mat):
7            count=sum(row)
8            heapq.heappush(soldiers,(count,i))
9            
10        res=[]
11
12        for _ in range(k):
13            count, i = heapq.heappop(soldiers)
14            res.append(i)
15
16        return res        
17
18        