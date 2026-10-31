# Last updated: 31/10/2026, 19:03:01
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
        