# Last updated: 10/12/2025, 07:39:46
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e_sum=0
        d_sum=0
        d_sum = sum((map(int, ''.join(map(str,nums)))))
        for i in nums:
            e_sum +=i 
        return (e_sum-d_sum)