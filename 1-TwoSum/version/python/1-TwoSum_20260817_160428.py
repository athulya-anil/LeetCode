# Last updated: 17/08/2026, 16:04:28
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        for i in range(len(nums)):
9            for j in range(1,len(nums)):
10                if nums[i]+nums[j] == target:
11                    if i<j:
12                        return([i,j])
13
14        