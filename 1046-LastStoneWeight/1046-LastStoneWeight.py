# Last updated: 30/03/2026, 18:31:18
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
14            largest=heapq.heappop(stones)    
15            second_largest=heapq.heappop(stones)    
16
17            if second_largest != largest:
18                heapq.heappush(stones, largest-second_largest)
19
20        if len(stones)==1:
21            return(-heapq.heappop(stones))
22        else:
23            return 0            
24
25            
26
27
28        