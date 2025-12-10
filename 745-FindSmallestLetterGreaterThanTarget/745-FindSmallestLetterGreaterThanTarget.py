# Last updated: 10/12/2025, 07:41:18
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        beg=0
        end=len(letters)-1
        while beg<=end:
            mid=(beg+end)//2
            if letters[mid] <= target:
                beg=mid+1
            else: 
                end=mid-1
        return(letters[beg%len(letters)])         

    