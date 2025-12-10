# Last updated: 10/12/2025, 07:39:39
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = Counter(sub)
            
            # Sort by frequency (desc), then value (desc)
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            # Pick top x elements
            top_x = [num for num, _ in sorted_items[:x]]
            
            # Compute sum of all occurrences of top x elements
            total = sum(val for val in sub if val in top_x)
            ans.append(total)
        
        return ans
    