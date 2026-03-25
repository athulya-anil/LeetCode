# Last updated: 25/03/2026, 15:44:36
1import heapq
2class Solution(object):
3    def findKthLargest(self, nums, k):
4        """
5        :type nums: List[int]
6        :type k: int
7        :rtype: int
8        """
9        min_heap=[]
10        for num in nums:
11            if len(min_heap)<k:
12                heapq.heappush(min_heap,num)
13            else:
14                heapq.heappushpop(min_heap,num)    
15
16        return(min_heap[0])        
17
18        