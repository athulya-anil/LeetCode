# Last updated: 25/08/2026, 12:10:07
1class Solution(object):
2    def searchRange(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        def first_pos():
9            beg=0
10            end=len(nums)-1
11            while beg<=end:
12                mid=(beg+end)//2
13                if nums[mid]<target:
14                    beg=mid+1
15                else:
16                    end=mid-1    
17            return(beg)
18        def last_pos():
19            beg=0
20            end=len(nums)-1
21            while beg<=end:
22                mid=(beg+end)//2
23                if nums[mid]<=target:
24                    beg=mid+1
25                else:
26                    end=mid-1    
27            return(end)    
28        first=first_pos()
29        if first == len(nums) or nums[first] != target:
30            return([-1,-1])
31        last=last_pos()    
32        return([first,last])    