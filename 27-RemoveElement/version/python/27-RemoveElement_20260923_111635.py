# Last updated: 23/09/2026, 11:16:35
1class Solution:
2    def removeElement(self, nums: list[int], val: int) -> int:
3        slow=fast=0
4        while fast<len(nums):
5            if nums[fast]!=val:
6                nums[slow],nums[fast]=nums[fast],nums[slow]
7                slow+=1
8            fast+=1
9        return slow        