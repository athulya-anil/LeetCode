# Last updated: 31/10/2026, 21:14:55
1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        beg=0
4        end=num
5        while beg<=end:
6            mid=(beg+end)//2
7            sq=mid*mid
8
9            if sq==num:
10                return True
11            elif sq<num:
12                beg=mid+1
13            else:
14                end=mid-1
15                
16        return False                
17        