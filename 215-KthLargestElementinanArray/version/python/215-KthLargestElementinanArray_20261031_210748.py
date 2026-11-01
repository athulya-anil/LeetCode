# Last updated: 31/10/2026, 21:07:48
1import heapq
2
3class Solution:
4    def findKthLargest(self, nums: list[int], k: int) -> int:
5        heap=[]
6        for i in range(len(nums)):
7            if len(heap)<k:
8                heapq.heappush(heap,nums[i])
9            else:
10                heapq.heappushpop(heap,nums[i])
11
12        return heapq.heappop(heap)            
13        