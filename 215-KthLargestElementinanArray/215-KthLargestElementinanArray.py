# Last updated: 30/03/2026, 20:04:57
1import heapq
2class Solution(object):
3    def findKthLargest(self, nums, k):
4        """
5        :type nums: List[int]
6        :type k: int
7        :rtype: int
8        """
9        heap=[]
10        for num in nums:
11            if len(heap)<k:
12                heapq.heappush(heap,num)
13            else:
14                heapq.heappushpop(heap,num)    
15
16        return(heapq.heappop(heap))        