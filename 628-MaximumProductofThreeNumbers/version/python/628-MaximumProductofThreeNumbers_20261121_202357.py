# Last updated: 21/11/2026, 20:23:57
1class Solution:
2    def maximumProduct(self, nums: list[int]) -> int:
3        nums.sort()
4        top3=nums[-1]*nums[-2]*nums[-3]
5        bottom2=nums[0]*nums[1]*nums[-1]
6        return max(top3,bottom2)
7
8        