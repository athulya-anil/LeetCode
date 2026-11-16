# Last updated: 15/11/2026, 21:19:41
1from collections import Counter
2class Solution:
3    def longestConsecutive(self, nums: list[int]) -> int:
4        nums=set(nums)
5        longest=0
6        for num in nums:
7            if (num - 1) not in nums:
8                next_num = num + 1
9                length=1
10                while next_num in nums:
11                    length+=1
12                    next_num+=1
13                longest=max(length, longest)
14        return longest            
15
16
17        