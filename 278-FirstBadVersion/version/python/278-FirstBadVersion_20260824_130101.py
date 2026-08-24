# Last updated: 24/08/2026, 13:01:01
1# The isBadVersion API is already defined for you.
2# @param version, an integer
3# @return a bool
4# def isBadVersion(version):
5
6class Solution(object):
7    def firstBadVersion(self, n):
8        """
9        :type n: int
10        :rtype: int
11        """
12        beg=1
13        end=n
14        while beg<=end:
15            mid=(beg+end)//2
16            if isBadVersion(mid)==False:
17                beg=mid+1
18            else:
19                end=mid-1
20        return(beg)            
21        