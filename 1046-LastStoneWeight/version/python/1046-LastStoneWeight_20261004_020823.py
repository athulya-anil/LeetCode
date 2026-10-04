# Last updated: 04/10/2026, 02:08:23
1import heapq
2class Solution(object):
3    def lastStoneWeight(self, stones):
4        """
5        :type stones: List[int]
6        :rtype: int
7        """
8        for i in range(len(stones)):
9            stones[i]=-stones[i]
10
11        heapq.heapify(stones)    
12
13        while len(stones)>1:
14
15            largest_stone = heapq.heappop(stones)
16            second_stone = heapq.heappop(stones)
17            heapq.heappush(stones,(largest_stone-second_stone))
18
19
20        return -heapq.heappop(stones)    
21
22        