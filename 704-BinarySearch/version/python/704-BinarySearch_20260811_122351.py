# Last updated: 11/08/2026, 12:23:51
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        beg=0
9        end=len(nums) - 1
10
11        while beg<=end:
12            mid=(beg+end)/2
13            if nums[mid]==target:
14                return(mid)
15            elif nums[mid] < target:
16                beg=mid+1
17            else:
18                end=mid-1
19        return (-1)            