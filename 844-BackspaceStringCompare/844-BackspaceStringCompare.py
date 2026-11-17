# Last updated: 16/11/2026, 21:28:50
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1=[]
        st2=[]

        for char in s:
            if char != "#":
                st1.append(char)
            elif st1:
                st1.pop()

        for char in t:
            if char != "#":
                st2.append(char)
            elif st2:
                st2.pop()

        return st1==st2        
                    