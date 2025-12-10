# Last updated: 10/12/2025, 07:41:07
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(cap):
            load=0
            d=1
            for i in weights:
                if load + i > cap:
                    d+=1
                    load=0
                load+=i
            return (d<=days)    

        beg=max(weights)    
        end=sum(weights)
        ans=end
        while beg<=end:
            mid=(beg+end)//2
            if canShip(mid) == True:
                ans=mid
                end=mid-1
            else:
                beg=mid+1
        return(ans)        
