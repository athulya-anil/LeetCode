# Last updated: 10/12/2025, 07:40:28
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # n=max(arr)+k
        # missing_numbers=[]
        # for i in range (1,n+1):
        #     if i not in arr:
        #         missing_numbers.append(i)
        # return(missing_numbers[k-1])  

        n = max(arr) + k
        missing_numbers = []
        for i in range(1, n+1):
            if i not in arr:
                missing_numbers.append(i)
        return missing_numbers[k-1]
