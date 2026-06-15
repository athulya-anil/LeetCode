# Last updated: 14/06/2026, 23:03:20
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg=0
        end=n
        ans=0
        while beg<=end:
            mid=(beg+end)//2
            coins=mid*(mid+1)//2
            if coins<=n:
                ans=mid
                beg=mid+1
            else:
                end=mid-1     
        return(ans)      
        