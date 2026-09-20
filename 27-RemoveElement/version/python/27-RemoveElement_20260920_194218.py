# Last updated: 20/09/2026, 19:42:18
1class Solution:
2    def removeElement(self, nums: list[int], val: int) -> int:
3        fast=slow = 0
4        while fast<len(nums):
5            if nums[fast]!=val:
6                nums[fast],nums[slow]=nums[slow],nums[fast]
7                slow+=1
8            fast+=1
9        return slow           
10
11