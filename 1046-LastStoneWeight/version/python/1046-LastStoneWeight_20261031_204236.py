# Last updated: 31/10/2026, 20:42:36
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
12        while len(stones)>1:
13            first_largest = heapq.heappop(stones)
14            second_largest = heapq.heappop(stones)
15
16            if first_largest != second_largest:
17                new_weight = first_largest-second_largest
18                heapq.heappush(stones,new_weight)
19
20        if len(stones)==1:
21            return -heapq.heappop(stones)
22        else:
23            return 0  
24        