# Last updated: 01/11/2026, 15:04:11
1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        slow=fast=0
7
8        while fast<len(nums):
9            if nums[fast]!=0:
10                nums[slow],nums[fast]=nums[fast],nums[slow]
11                slow+=1
12            fast+=1
13        return nums    
14                
15        