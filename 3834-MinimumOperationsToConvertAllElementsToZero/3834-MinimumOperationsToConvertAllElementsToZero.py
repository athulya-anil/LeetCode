# Last updated: 10/12/2025, 07:39:37
class Solution(object):
    def minOperations(self, nums):
        total = 0          # total operations
        inc_stack = []           # monotonically increasing stack

        for v in nums:
            # pop larger tails to keep stack increasing
            while inc_stack and v < inc_stack[-1]:
                inc_stack.pop()

            # skip zeros; start a new layer only when value rises
            if v and (not inc_stack or v > inc_stack[-1]):
                inc_stack.append(v)
                total += 1

        return total
