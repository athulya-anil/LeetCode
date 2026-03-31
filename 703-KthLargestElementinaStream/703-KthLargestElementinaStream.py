# Last updated: 30/03/2026, 20:27:42
1import heapq
2class KthLargest(object):
3
4    def __init__(self, k, nums):
5        """
6        :type k: int
7        :type nums: List[int]
8        """
9        self.k=k
10        self.nums=nums
11
12        heapq.heapify(self.nums)
13
14        while len(self.nums) > self.k:
15            heapq.heappop(self.nums)
16
17    def add(self, val):
18        """
19        :type val: int
20        :rtype: int
21        """
22        if len(self.nums)<self.k:
23            heapq.heappush(self.nums,val)
24        else:
25            heapq.heappushpop(self.nums,val)
26
27        return(self.nums[0])        
28 
29
30
31        
32
33
34# Your KthLargest object will be instantiated and called as such:
35# obj = KthLargest(k, nums)
36# param_1 = obj.add(val)