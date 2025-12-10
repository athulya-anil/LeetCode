# Last updated: 10/12/2025, 07:40:00
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_balanced(num):
            s = str(num)
            if '0' in s: 
                return False
            
            counts = [0] * 10
            for c in s:
                counts[int(c)] += 1
            
            for c in s:
                if counts[int(c)] != int(c):
                    return False
            
            return True  # ← MISSING: Added this line
        
        num = n + 1  # ← MISSING: Added this line
        while True:
            if is_balanced(num):
                return num
            num += 1