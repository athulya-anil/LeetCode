# Last updated: 22/09/2026, 23:32:05
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        beg=1
11        end=n
12        while beg<=end:
13            mid=(beg+end)//2
14            if guess(mid)==0:
15                return mid
16            elif guess(mid)==-1:
17                end=mid-1
18            else:
19                beg=mid+1         