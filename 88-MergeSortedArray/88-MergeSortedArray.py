# Last updated: 10/07/2026, 12:00:27
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left=nums1[:m]
        f1=f2=slow=0
        while f1<m and f2<n:
            if left[f1]<nums2[f2]:
                nums1[slow]=left[f1]
                f1+=1
            else:
                nums1[slow]=nums2[f2]
                f2+=1   
            slow+=1

        while f1<m:
            nums1[slow]=left[f1]
            f1+=1
            slow+=1
        while f2<n:
            nums1[slow]=nums2[f2]  
            f2+=1
            slow+=1
        return(nums1)               
                

    