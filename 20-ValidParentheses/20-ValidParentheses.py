# Last updated: 10/07/2026, 12:01:01
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {'}':'{',')':'(',']':'['}

        for char in s:
            if char in pairs:
                top_element=stack.pop() if stack else '#'
                if top_element != pairs[char]:
                    return False
            else:    
                stack.append(char)
        return not stack      
        
       