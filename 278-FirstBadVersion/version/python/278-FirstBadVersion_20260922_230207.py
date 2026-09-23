# Last updated: 22/09/2026, 23:02:07
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        beg=0
7        end=n
8        while beg<end:
9            mid=(beg+end)//2
10
11            if isBadVersion(mid) == False:
12                beg=mid+1
13            else: 
14                end=mid
15        return beg        
16        