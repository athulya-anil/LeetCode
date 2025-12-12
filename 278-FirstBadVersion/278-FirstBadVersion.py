# Last updated: 12/12/2025, 09:22:59
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
14        ans=-1
15        while beg<=end:
16            mid=(beg+end)//2
17            if isBadVersion(mid)==False:
18                beg=mid+1
19            elif isBadVersion(mid)==True:   
20                ans=mid
21                end=mid-1
22        return(ans)         
23
24        