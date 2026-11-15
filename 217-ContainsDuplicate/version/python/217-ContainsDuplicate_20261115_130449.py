# Last updated: 15/11/2026, 13:04:49
1from collections import Counter 
2class Solution:
3    def containsDuplicate(self, nums: list[int]) -> bool:
4        list1=Counter(nums)
5        for value in list1.values():
6            if value >1:
7                return True
8        return False        
9        