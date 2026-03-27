# Last updated: 27/03/2026, 00:08:07
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
11        ls=[]
12        for x,y in points:
13            d=dist(x,y)
14            if len(ls) < k:
15                heapq.heappush(ls,(-d,x,y))
16            else:
17                heapq.heappushpop(ls,(-d,x,y))
18
19        return [[x,y] for d,x,y in ls]           
20
21
22
23        