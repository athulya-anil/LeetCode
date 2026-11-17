# Last updated: 16/11/2026, 21:19:26
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if stack and stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)
                
        return ''.join(c for c in stack)            
        