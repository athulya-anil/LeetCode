# Last updated: 24/08/2026, 12:46:59
1class Solution(object):
2    def mySqrt(self, x):
3        beg=1
4        end=x
5        while beg<=end:
6            mid=(beg+end)//2
7            sq=mid*mid
8            if sq==x:
9                return(mid)
10            elif sq<x:
11                beg=mid+1
12            else:
13                end=mid-1
14        return(end)            
15
16        