# Last updated: 30/03/2026, 20:38:58
1import heapq
2class Solution(object):
3    def kClosest(self, points, k):
4        """
5        :type points: List[List[int]]
6        :type k: int
7        :rtype: List[List[int]]
8        """
9        heap=[]
10        for x,y in points:
11            d=x**2+y**2
12            if len(heap)<k:
13                heapq.heappush(heap,(-d,x,y))
14            else:
15                heapq.heappushpop(heap,(-d,x,y))
16
17        return [[x,y] for d,x,y in heap]        