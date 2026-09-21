# Last updated: 21/09/2026, 15:54:43
1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        slow=fast=0
7        while fast<len(nums):
8            if nums[fast]!=0:
9                nums[fast], nums[slow]=nums[slow], nums[fast]
10                slow+=1
11            fast+=1
12        return nums        