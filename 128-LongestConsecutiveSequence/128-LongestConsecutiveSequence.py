# Last updated: 16/11/2026, 21:31:40
from collections import Counter
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        longest=0
        for num in nums:
            if (num - 1) not in nums:
                next_num = num + 1
                length=1
                while next_num in nums:
                    length+=1
                    next_num+=1
                longest=max(length, longest)
        return longest            


        