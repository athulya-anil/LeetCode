# Last updated: 14/06/2026, 23:01:38
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for i in operations:
            if i == "--X" or i == "X--":
                x-=1
            else:
                x+=1

        return(x)            
        