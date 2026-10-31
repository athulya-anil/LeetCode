# Last updated: 31/10/2026, 19:08:42
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """    
        beg=0
        end=len(letters)-1
        
        if target>=letters[-1]:
            return(letters[0])

        while beg<end:
            mid=(beg+end)//2
            if letters[mid] <= target:
                beg=mid+1
            else:
                end=mid
        return(letters[end])              

    