# Last updated: 10/07/2026, 12:00:50
class Solution(object):
    def mySqrt(self, x):
        beg=1
        end=x
        while beg<=end:
            mid=(beg+end)//2
            sq=mid*mid
            if sq==x:
                return mid
            elif sq<x:
                beg=mid+1
            else:
                end=mid-1
        return end               
        