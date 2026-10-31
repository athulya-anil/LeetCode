# Last updated: 31/10/2026, 19:02:10
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