# Last updated: 10/12/2025, 07:41:56
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg=1
        end=n
        while beg<end:
            mid=(beg+end)//2
            if isBadVersion(mid) != True: # not bad
                beg=mid+1
            else:
                end=mid    
        return(beg)        
        