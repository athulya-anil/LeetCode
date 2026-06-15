# Last updated: 14/06/2026, 23:02:51
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        beg=1
        end=max(piles)
        while beg<=end:
            mid=(beg+end)//2
            hours=0
            for p in piles:
                hours += (p + mid - 1)//mid
            if hours>h:
                beg=mid+1
            else:
                end=mid-1
        return (beg)            

       