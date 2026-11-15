# Last updated: 15/11/2026, 14:03:57
1from collections import Counter
2class Solution:
3    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
4        nums1=Counter(nums1)
5        res=[]
6
7        for char in nums2:
8            if char in nums1 and nums1[char]>0:
9                res.append(char)
10                nums1[char]-=1
11
12        return res
13        