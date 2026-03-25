# Last updated: 24/03/2026, 21:50:42
1import heapq
2class Solution(object):
3    def findKthLargest(self, nums, k):
4        """
5        :type nums: List[int]
6        :type k: int
7        :rtype: int
8        """
9        n=len(nums)
10        for i in range(n):
11            nums[i]=-nums[i]
12
13        heapq.heapify(nums)
14
15        for i in range(k-1):
16            heapq.heappop(nums)    
17
18        return(-heapq.heappop(nums))    
19        