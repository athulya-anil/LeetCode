# Last updated: 16/11/2026, 21:17:35
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums=Counter(nums)
        max_value=0
        res=[]
        max_value = max(nums.values())
        sum1=0
        for value in nums.values():
            if value == max_value:
                sum1+=value        
        return (sum1)       
