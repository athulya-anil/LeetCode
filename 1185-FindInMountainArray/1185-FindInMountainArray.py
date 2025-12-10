# Last updated: 10/12/2025, 07:40:53
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        #finding peak
        beg=0
        end=mountainArr.length()-1
        while beg<end:
            mid=(beg+end)//2
            if mountainArr.get(mid)<=mountainArr.get(mid+1):
                beg=mid+1
            else:
                end=mid    
        peak = beg   
        
        #find element in first half
        l=0
        r=peak
        ans=[]
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m)
            if val == target:
                return(m)
            elif val < target:
                l=m+1
            else:
                r=m-1     

        #find element in second half    
        l=peak
        r=mountainArr.length()-1        
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m) 
            if val == target:
                return(m)
            elif val > target:
                l=m+1
            else:
                r=m-1             
        return(-1)



                    

        

