# Last updated: 01/11/2026, 15:47:20
1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        stack = []
8        pairs = {'}':'{',')':'(',']':'['}
9
10        for char in s:
11            if char in pairs:
12                top_element=stack.pop() if stack else '#'
13                if top_element != pairs[char]:
14                    return False
15            else:    
16                stack.append(char)
17        return not stack      
18        
19       