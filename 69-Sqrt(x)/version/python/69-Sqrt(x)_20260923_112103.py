# Last updated: 23/09/2026, 11:21:03
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        beg=1
4        end=x
5        while beg<=end:
6            mid=(beg+end)//2
7            sq=mid*mid
8            if sq==x:
9                return mid
10            elif sq < x:
11                beg=mid+1
12            else:
13                end=mid-1
14        return end                
15
16        