# Last updated: 14/06/2026, 23:03:44
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap,num)
            else:
                heapq.heappushpop(heap,num)    

        return(heapq.heappop(heap))        