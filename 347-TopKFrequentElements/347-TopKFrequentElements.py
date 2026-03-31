# Last updated: 30/03/2026, 20:34:15
1import heapq
2from collections import Counter
3
4class Solution(object):
5    def topKFrequent(self, nums, k):
6        """
7        :type nums: List[int]
8        :type k: int
9        :rtype: List[int]
10        """
11        counter=Counter(nums)
12        heap=[]
13
14        for element,freq in counter.items():
15            if len(heap)<k:
16                heapq.heappush(heap,(freq,element))
17            else:
18                heapq.heappushpop(heap,(freq,element))    
19
20        return [element for freq,element in heap]
21        