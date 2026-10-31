# Last updated: 31/10/2026, 19:05:53
import heapq
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        soldiers = []

        for i,row in enumerate(mat):
            count=sum(row)
            heapq.heappush(soldiers,(count,i))
            
        res=[]

        for _ in range(k):
            count, i = heapq.heappop(soldiers)
            res.append(i)

        return res        

        