# Last updated: 10/12/2025, 07:41:49
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x=num
        if x<=1:
            return(True)
        beg=1
        end=x    
        while beg<=end:
            mid=(beg+end)//2
            sq=mid*mid
            if sq == x:
                return(True)
            elif sq < x:
                beg=mid+1
            else:
                end=mid-1
        return(False)                
        