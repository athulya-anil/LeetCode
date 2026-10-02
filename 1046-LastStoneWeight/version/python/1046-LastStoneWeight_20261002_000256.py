# Last updated: 02/10/2026, 00:02:56
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
15            first_element = heapq.heappop(stones)
16            second_element = heapq.heappop(stones)
17
18            if first_element != second_element:
19                new_element = first_element-second_element
20                heapq.heappush(stones,new_element) 
21
22        if stones:
23            return -heapq.heappop(stones)    
24        else:
25            return 0        
26
27        