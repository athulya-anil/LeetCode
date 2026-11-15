# Last updated: 15/11/2026, 14:17:05
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        freak={}
4        for i, n in enumerate(nums):
5            if target-n in freak:
6                return [freak[target-n],i]
7            freak[n]=i    
8        return []    
9        