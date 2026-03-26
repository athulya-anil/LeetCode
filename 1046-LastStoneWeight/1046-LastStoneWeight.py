# Last updated: 26/03/2026, 17:32:39
1import heapq
2
3class Solution(object):
4    def lastStoneWeight(self, stones):
5        """
6        :type stones: List[int]
7        :rtype: int
8        """
9
10        n=len(stones)
11        for i in range(n):
12            stones[i]=-stones[i]
13
14        heapq.heapify(stones)
15
16        while len(stones)>1:
17            largest=heapq.heappop(stones)
18            second_largest=heapq.heappop(stones)
19            if second_largest != largest:
20                heapq.heappush(stones, largest-second_largest) # -8 +7
21
22        if len(stones)==1:
23            return(-heapq.heappop(stones))
24        else:
25            return 0
26