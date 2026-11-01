# Last updated: 01/11/2026, 16:33:16
1class Solution:
2    def searchRange(self, nums: list[int], target: int) -> list[int]:
3        def first_pos():
4            first_pos=-1
5            beg=0
6            end=len(nums)-1
7            while beg<=end:
8                mid=(beg+end)//2
9                if nums[mid]==target:
10                    first_pos=mid
11                    end=mid-1
12                elif nums[mid]<target:
13                    beg=mid+1
14                elif nums[mid]>target:
15                    end=mid-1
16            return first_pos    
17
18        def last_pos():
19            last_pos=-1
20            beg=0
21            end=len(nums)-1
22            while beg<=end:
23                mid=(beg+end)//2
24                if nums[mid]==target:
25                    last_pos=mid
26                    beg=mid+1
27                elif nums[mid]<target:
28                    beg=mid+1
29                elif nums[mid]>target:
30                    end=mid-1
31            return last_pos    
32
33        return[first_pos(),last_pos()]    
34
35
36        