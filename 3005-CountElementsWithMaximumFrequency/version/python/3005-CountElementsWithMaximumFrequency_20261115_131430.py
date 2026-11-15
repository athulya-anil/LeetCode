# Last updated: 15/11/2026, 13:14:30
1from collections import Counter
2class Solution:
3    def maxFrequencyElements(self, nums: List[int]) -> int:
4        nums=Counter(nums)
5        max_value=0
6        res=[]
7        for value in nums.values():
8            if value>max_value:
9                max_value=value
10                
11        for key, value in nums.items():
12            if value == max_value:
13                res.append(value)
14        sum=0
15        for i in res:
16            sum+=i        
17        return (sum)       
18