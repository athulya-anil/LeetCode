# Last updated: 24/08/2026, 14:00:16
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num):
7
8class Solution(object):
9    def guessNumber(self, n):
10
11        """
12        :type n: int
13        :rtype: int
14        """
15        beg=1
16        end=n
17        while beg<=end:
18            mid=(beg+end)//2
19            if guess(mid)==0:
20                return(mid)
21            elif guess(mid)==1:
22                beg=mid+1
23            else:
24                end=mid-1       