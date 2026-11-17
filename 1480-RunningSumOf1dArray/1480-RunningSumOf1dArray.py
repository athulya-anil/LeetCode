# Last updated: 16/11/2026, 21:18:45
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res=[]
        sum1=0
        for n in nums:
            sum1+=n
            res.append(sum1)
        return (res)    
        