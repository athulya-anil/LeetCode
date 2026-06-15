# Last updated: 14/06/2026, 23:03:19
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        slow = 0
        
        while slow < len(chars):
            fast = slow
            while fast < len (chars) and chars[slow]==chars[fast]:
                fast += 1
            
            chars[write]=chars[slow]
            write +=1

            length = fast - slow

            if length>1:
                for digits in str(length):
                    chars[write]=digits
                    write +=1

            slow=fast  
        return (len(chars[:write]))          


        
        