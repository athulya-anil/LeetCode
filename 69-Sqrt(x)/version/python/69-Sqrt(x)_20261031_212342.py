# Last updated: 31/10/2026, 21:23:42
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        beg=0
4        end=x
5
6        while beg<=end:
7            mid=(beg+end)//2
8            sq=mid*mid
9
10            if sq == x:
11                return mid
12            elif sq > x:
13                end = mid-1
14            else:
15                beg=mid+1
16
17        return end            
18        