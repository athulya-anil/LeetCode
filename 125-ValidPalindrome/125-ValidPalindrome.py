# Last updated: 10/12/2025, 07:42:39
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s = ''.join(c for c in s if c.isalnum())
        # def sw(l,r):
        #     if l>=r:
        #         return True
        #     if s[l]!=s[r]:
        #         return False
        #     return sw(l+1,r-1)    
        # return sw(0,len(s)-1)    
        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]:
                return(False)
            l+=1
            r-=1
        return(True)        