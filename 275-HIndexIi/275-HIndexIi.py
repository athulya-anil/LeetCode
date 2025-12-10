# Last updated: 10/12/2025, 07:41:58
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        beg=0
        end=len(citations)-1
        n=len(citations)
        while beg<=end:
            mid=(beg+end)//2
            if citations[mid] >= n-mid:
                end=mid-1
            else:
                beg=mid+1
        return(n-beg)    
                