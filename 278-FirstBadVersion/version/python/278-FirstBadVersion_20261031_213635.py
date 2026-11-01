# Last updated: 31/10/2026, 21:36:35
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        beg=1
7        end=n
8
9        while beg<end:
10            mid=(beg+end)//2
11            if isBadVersion(mid) == False:
12                beg=mid+1
13            else:
14                end=mid
15        return end            
16        