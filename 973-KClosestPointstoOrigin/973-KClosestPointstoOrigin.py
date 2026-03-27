# Last updated: 27/03/2026, 14:50:16
1import heapq
2class Solution(object):
3    def kClosest(self, points, k):
4        """
5        :type points: List[List[int]]
6        :type k: int
7        :rtype: List[List[int]]
8        """
9        def dist(x,y):
10            return(x**2+y**2)
11        heap=[]
12        for x,y in points:
13            d=dist(x,y)
14        
15
16            if len(heap) < k:
17                heapq.heappush(heap,(-d,x,y))
18            else:
19                heapq.heappushpop(heap,(-d,x,y))    
20
21        return[[x,y] for d,x,y in heap]    