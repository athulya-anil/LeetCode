# Last updated: 26/03/2026, 13:29:24
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
11        heap = []
12        counter=Counter(nums)
13
14        for key, freq in counter.items():
15            if len(heap)<k:
16                heapq.heappush(heap,(freq,key))
17            else:
18                heapq.heappushpop(heap,(freq,key))    
19
20        return [num for freq, num in heap]        