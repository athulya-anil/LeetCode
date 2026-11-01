# Last updated: 31/10/2026, 20:30:59
1from collections import Counter
2import heapq
3class Solution:
4    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
5        nums1=Counter(nums)
6        heap=[]
7        for val, count in nums1.items():
8            heapq.heappush(heap,(count,val))
9
10            if len(heap)>k:
11                heapq.heappop(heap)
12
13        res=[]
14        for _ in range(len(heap)):
15            count,val = heapq.heappop(heap)       
16            res.append(val) 
17
18        return res    
19
20        