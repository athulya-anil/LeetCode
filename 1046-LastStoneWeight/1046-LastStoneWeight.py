# Last updated: 25/03/2026, 15:22:18
1import heapq
2
3class Solution(object):
4    def lastStoneWeight(self, stones):
5        """
6        :type stones: List[int]
7        :rtype: int
8        """
9        n=len(stones)
10        for i in range(n):
11            stones[i]=-stones[i]
12
13        heapq.heapify(stones)
14        while len(stones)>1:
15            largest=heapq.heappop(stones)
16            second_largest=heapq.heappop(stones)
17            if second_largest != largest:
18                heapq.heappush(stones,largest-second_largest)
19
20        if len(stones) == 1:
21            return(-heapq.heappop(stones))
22        else:
23            return 0        
24
25
26
27
28        