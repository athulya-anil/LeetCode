# Last updated: 15/11/2026, 13:17:18
1from collections import Counter
2class Solution:
3    def maxFrequencyElements(self, nums: List[int]) -> int:
4        nums=Counter(nums)
5        max_value=0
6        res=[]
7        max_value = max(nums.values())
8        sum1=0
9        for value in nums.values():
10            if value == max_value:
11                sum1+=value        
12        return (sum1)       
13