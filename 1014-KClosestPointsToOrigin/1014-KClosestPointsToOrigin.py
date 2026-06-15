# Last updated: 14/06/2026, 23:02:44
import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for x,y in points:
            d=x**2+y**2
            if len(heap)<k:
                heapq.heappush(heap,(-d,x,y))
            else:
                heapq.heappushpop(heap,(-d,x,y))

        return [[x,y] for d,x,y in heap]        