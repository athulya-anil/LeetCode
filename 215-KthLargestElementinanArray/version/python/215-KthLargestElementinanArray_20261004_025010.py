# Last updated: 04/10/2026, 02:50:10
1import heapq
2class Solution:
3    def findKthLargest(self, nums: list[int], k: int) -> int:
4        heap=[]
5        for num in nums:
6            if len(heap)<k:
7                heapq.heappush(heap,num)
8            else:
9                heapq.heappushpop(heap,num)
10                
11        return(heapq.heappop(heap))            
12            
13