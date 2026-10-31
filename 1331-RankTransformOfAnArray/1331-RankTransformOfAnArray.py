# Last updated: 31/10/2026, 19:06:54
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = sorted(arr)
        rank = {}
        r = 1

        for num in n:
            if num not in rank:
                rank[num] = r
                r += 1
        
        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        
        return arr
        