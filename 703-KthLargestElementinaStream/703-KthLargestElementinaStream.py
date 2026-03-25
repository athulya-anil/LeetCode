# Last updated: 25/03/2026, 16:59:07
1import heapq
2class KthLargest(object):
3
4    def __init__(self, k, nums):
5        """
6        :type k: int
7        :type nums: List[int]
8        """
9        self.k=k
10        self.min_heap=nums
11
12        heapq.heapify(self.min_heap)
13
14        while len(self.min_heap) > k:
15            heapq.heappop(self.min_heap) 
16        
17    def add(self, val):
18        """
19        :type val: int
20        :rtype: int
21        """
22        heapq.heappush(self.min_heap,val)
23        if len(self.min_heap) > self.k:
24            heapq.heappop(self.min_heap) 
25        return(self.min_heap[0])    
26        
27
28
29# Your KthLargest object will be instantiated and called as such:
30# obj = KthLargest(k, nums)
31# param_1 = obj.add(val)