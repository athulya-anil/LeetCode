# Last updated: 15/11/2026, 13:57:22
1
2class Solution:
3    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
4        nums1=set(nums1)
5        nums2=set(nums2)
6        return (list(nums1 & nums2))        