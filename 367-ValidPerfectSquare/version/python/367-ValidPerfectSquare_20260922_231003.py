# Last updated: 22/09/2026, 23:10:03
1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        beg=1
4        end=num
5        while beg<=end:
6            mid=(beg+end)//2
7            sq=mid*mid
8            if sq == num:
9                return True
10            elif sq<num:
11                beg=mid+1
12            else:
13                end=mid-1
14                
15        return False                
16        