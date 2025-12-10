# Last updated: 10/12/2025, 07:41:13
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
        ans=0
        while beg<=end:
            mid=(beg+end)//2
            time_taken=0
            for i in piles:
                time_taken += (i + mid-1)//mid #ciel
            if time_taken > h:
                beg=mid+1
            else:
                ans=mid
                end=mid-1        
        return(ans)