# Last updated: 14/11/2026, 21:16:20
1class Solution:
2    def runningSum(self, nums: list[int]) -> list[int]:
3        res=[]
4        sum1=0
5        for n in nums:
6            sum1+=n
7            res.append(sum1)
8        return (res)    
9        