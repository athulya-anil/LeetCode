# Last updated: 24/08/2026, 12:42:42
1class Solution(object):
2    def mySqrt(self, x):
3        beg=0
4        end=x
5        while beg<=end:
6            mid=(beg+end)//2
7            sq=mid*mid
8            if sq==x:
9                return(mid)
10            elif sq<x:
11                b=mid
12                beg=mid+1
13            else:
14                end=mid-1
15        return(b)            
16
17        