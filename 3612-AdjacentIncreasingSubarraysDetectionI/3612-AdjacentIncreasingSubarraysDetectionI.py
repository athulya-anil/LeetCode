# Last updated: 10/12/2025, 07:39:38
class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        
        # Helper to check if subarray nums[i : i+k] is strictly increasing
        def is_increasing(i):
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    return False
            return True
        
        # Check pairs of adjacent subarrays
        for i in range(n - 2 * k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True
        
        return False

        