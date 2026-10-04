# Last updated: 04/10/2026, 02:36:10
1from collections import Counter
2import heapq
3class Solution:
4    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
5        nums_count = Counter(nums)
6        heap=[]
7
8        for key,value in nums_count.items():
9            if len(heap)<k:
10                heapq.heappush(heap,(value,key))
11            else:
12                heapq.heappushpop(heap,(value,key))    
13
14        return [h[1] for h in heap]