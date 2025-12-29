# Last updated: 29/12/2025, 23:33:09
1import math
2class Solution(object):
3    def minEatingSpeed(self, piles, h):
4        """
5        :type piles: List[int]
6        :type h: int
7        :rtype: int
8        """
9        beg=1
10        end=max(piles)
11        while beg<=end:
12            mid=(beg+end)//2
13            hours=0
14            for p in piles:
15                hours += (p + mid - 1)//mid
16            if hours>h:
17                beg=mid+1
18            else:
19                end=mid-1
20        return (beg)            
21
22       