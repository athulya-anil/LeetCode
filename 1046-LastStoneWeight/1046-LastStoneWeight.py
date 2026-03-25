# Last updated: 24/03/2026, 21:41:48
1import heapq
2
3class Solution(object):
4    def lastStoneWeight(self, stones):
5        """
6        :type stones: List[int]
7        :rtype: int
8        """
9        n=len(stones)
10        for i in range (n):
11            stones[i]=-stones[i]
12
13        heapq.heapify(stones)    
14
15        while len(stones) > 1:
16
17            largest=heapq.heappop(stones)
18            second_largest=heapq.heappop(stones)
19
20            if largest != second_largest:
21                heapq.heappush(stones,largest - second_largest)
22
23        if len(stones)==1:
24            return(-stones[0])
25        else:
26            return 0        
27        