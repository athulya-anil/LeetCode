# Last updated: 16/11/2026, 21:30:07
from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1=Counter(nums1)
        res=[]

        for char in nums2:
            if char in nums1 and nums1[char]>0:
                res.append(char)
                nums1[char]-=1

        return res
        